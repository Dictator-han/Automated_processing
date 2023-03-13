#coding;utf-8

import pandas as pd

from robot_settings import DATABASES, DATABASE_CON_INFOS



def get_db_engine(db_user):
    """
    获取数据库连接接口
    :param db_user:
    :return:
    """
    return DATABASES[db_user]['ENGINE']

def select(sql, db_user='default'):
    DB_ENGINE = get_db_engine(db_user)
    if DB_ENGINE == 'mysql' :
        import pymysql
        con = pymysql.connect(
            **DATABASE_CON_INFOS[db_user]
        )   # 连接数据库
    else:
        raise Exception('请勿使用MYSQL之外的引擎')
    df = pd.read_sql(con=con, sql=sql) #查询取数
    return df