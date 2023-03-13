import warnings
import datetime
from datetime import timedelta
import os
from settings import DATABASE_CON_INFOS
import pandas as pd
import pymysql

#声明
warnings.filterwarnings('ignore')
today = datetime.date.today()
yesterday = datetime.date.today() + timedelta(days=-1)
#定义文件夹
def filter():
    path = 'D:\\日报\\每日数据'
    file_path = path + '\\' + str(today)
    if not os.path.exists(file_path):
        os.mkdir(file_path)
        print("创建成功")
    else:
        print('文件夹已存在')

#定义取数

def select(sql):
    con = pymysql.connect(
        **DATABASE_CON_INFOS['default']
    )
    df = pd.read_sql(con= con ,sql= sql)
    return df