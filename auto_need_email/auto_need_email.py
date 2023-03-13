# -*- coding: utf-8 -*-
import pandas as pd
import pandas.io.formats.excel
from xlsxpandasformatter import FormattedWorksheet
import seaborn as sns
from settings import DATABASE_CON_INFOS,email_dict,SQL_dict
from missions import today,filter
#系统库
import datetime
from datetime import timedelta
import win32com.client as win32
import warnings
import os
from dateutil.relativedelta import relativedelta
#连接数据库的pyhton库
import pymysql.cursors


class Auto_need_email():
    def __init__(self,file_name,file_path,SQL_dict,email_dict,**kwargs):
        self.file_name = file_name
        self.file_path = file_path
        self.SQL_dict = SQL_dict
        self.kwargs = kwargs
        self.email_dict = email_dict

    # 生成文件
    def file(self,SQL_dict,file_path):
        for name,sql in SQL_dict:
            excel_name = name + str(today) + '.xlsx'
            excel_path = file_path + '\\' + excel_name



    def sql(self,SQL_dict):
        for name,sql in self.SQL_dict:
            print(sql)
            df = self.select(sql)

    def select(self,sql):
        import pymysql
        con = pymysql.connect(
            **DATABASE_CON_INFOS['default']
        )
        df = pd.read_sql(con=con, sql=sql)
        return df

    def run(self):
        try:
            self.select()
        except Exception as e:
            raise e
