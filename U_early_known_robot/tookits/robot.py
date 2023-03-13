#encoding utf8
#editor by qiqi

import xlwings as xw #表格处理
import requests #发送图片
import json #图片处理
import base64 #编码解码，图片处理
import os,time
from PIL import ImageGrab
from tookits.db_operator import select #连接数据库，取数
from robot_settings import RESULT_DIR, MODEL_DIR, REPORT_DATE #机器人设置，包括文件路径



class EarlyKnownRobot():
    """
    方法：
        调用存储过程
        数据存储到固定位置
        截图为图片
        读取图片
        发送图片到接口
        run方法
    """


    def __init__(self,  SQL_dict, PIC_dict, API_dict, file_name, **kwargs):
        self.file_name = file_name
        self.SQL_dict = SQL_dict
        self.PIC_dict = PIC_dict
        self.API_dict = API_dict
        self.kwargs = kwargs
        self.params() #参数包


    def params(self):
        """
        默认参数设置
        data_sheet:数据源sheet，不传入则默认叫“数据源”
        :return:
        """
        if 'data_sheet' in self.kwargs.keys():
            self.data_sheet = self.kwargs['data_sheet']
        else:
            self.data_sheet = '分天明细' #已修改
        if 'db_user' in self.kwargs.keys():
            self.db_user = self.kwargs['db_user']
        else:
            self.db_user = 'default'
        if 'file_path' in self.kwargs.keys():
            self.file_path = self.kwargs['file_path']
        else:
            self.file_path = MODEL_DIR
        self.app = xw.App(visible=True,
                          add_book=False)  # 指定是在桌面显示
        self.wb = self.app.books.open(os.path.join(self.file_path, self.file_name))  # 打开文件
        return self


    def call_proc_statement(self, sql):
        """
        调用存储过程
        :return:
        """
        sql = "call {}".format(sql)
        return select(sql)


    def excel_catch_screen(self, report_sheet, screen_area):
        """
        生成图片
        :return:
        """
        ws = self.wb.sheets[report_sheet]  # 选择sheet
        ws.range(screen_area).api.CopyPicture(Format=2)  # 复制图片区域
        img = ImageGrab.grabclipboard()  # 获取剪贴板的图片数据
        img_name = os.path.join(RESULT_DIR, report_sheet + REPORT_DATE+ ".PNG")  # 生成图片的文件名
        print(img_name)
        img.save(img_name)  # 保存图片


    def read_pic_to_json(self, pic_path):
        """
        读取图片并转换为json格式
        :return:
        """
        with open(pic_path, "rb") as f:
            base64_data = base64.b64encode(f.read())
        # 格式化消息
        data = {
            "message": {
                "body": [
                    {
                        "content": base64_data.decode('utf-8'),
                        "type": "IMAGE"
                    }
                ]
            }
        }

        return json.dumps(data)


    def send_pic_to_API(self):
        """
        将图片推送给机器人
        :return:
        """
        for url, pic_list in self.API_dict.items():
            for pic in pic_list:
                requests.post(url, data=self.read_pic_to_json(
                    os.path.join(RESULT_DIR, pic + REPORT_DATE + '.PNG')),
                              headers={'Content-Type': 'application/json'}
                              )

    def insert_data_to_file(self):
        sht = self.wb.sheets[self.data_sheet]
        for sql, range in self.SQL_dict.items():
            print(sql)
            sht.range(range[1]).clear_contents()  # 清空单元格
            df = self.call_proc_statement(sql)  # 读取存储过程
            sht.range(range[0]).value = df  # 把DF写在对应位置
            time.sleep(30)
            self.wb.api.RefreshAll() ##刷新整个数据表

        for sheet, report_area in self.PIC_dict.items():
            try:
                self.excel_catch_screen(sheet, report_area)
            except:
                print(f"{sheet}存储失败，可能为sheet名不存在")
        return self


    def run(self):
        try:
            self.insert_data_to_file()
            self.wb.save()
            self.wb.close()
            self.app.quit()
            self.send_pic_to_API()
        except Exception as e:
            raise e