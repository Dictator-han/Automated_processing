from tookits.robot import EarlyKnownRobot


SQL_dict = {
        # 先清除早知道模板中固定位置数据（一般为昨日数据），再写入
        # 'U4_daily_report_robot_ensemble_trend':['A2', 'A2:D94'],   # A2：数据写入起始位置，  A2:D94:报表文件清除数据区域
        # 'U4_daily_report_robot_ensemble_main_target':['H2', 'H2:AB17'],
        # 'U4_daily_report_robot_ensemble_industry':['AD2', 'AD2:AS40'],
        # 'U4_daily_report_robot_ensemble_main_cust':['AU2','AU2:BJ60'],
        # 'U4_daily_report_robot_ensemble_rise_cust':['BN2','BN2:BV8'],
        # 'U4_daily_report_robot_ensemble_fall_cust':['BY2', 'BY2:CG8'],
        'u5_daily_2':['A1','A:L']
    }

PIC_dict = {
    'U5早知道': 'M1: W85',  # sheet：截图区域（默认sheet名为图片存储名称）
    'U5早知道-任务': 'A1: K97',  # sheet：截图区域（默认sheet名为图片存储名称）
    # 'U5部门早知道': 'M1: W85',  # sheet：截图区域（默认sheet名为图片存储名称）
}

API_dict = {
    # 'http://apiin.im.baidu.com/api/msg/groupmsgsend?access_token=d593936af266a8a10afa7ffd1244265e9': ['U5早知道'],    # API：[图片列表]
    # '': ['U5早知道'],    # 测试
    # '': ['U5早知道-任务']    # 测试
}

EarlyKnownRobot(SQL_dict=SQL_dict,
                PIC_dict=PIC_dict,
                API_dict=API_dict,
                # file_name='【DEMO】U5_ensemble.xlsx'  # 早知道Excel模板
                file_name='【U5日报】3.xlsx'  # 早知道Excel模板
                ).run()