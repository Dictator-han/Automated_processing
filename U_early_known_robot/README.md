
<font face="微软雅黑" size=7>早知道模块</font>
***

## 1、结构介绍


```
├─model_files                          # 早知道模板存储位置
|  |  ****.xlsx                        # 早知道模板
│          
├─result_files                         # 早知道结果截图存储位置
|  |  ****.PNG                         # 早知道结果截图
│
├─tookits                               
|  |  db_operator.py                   # 数据库读取方法
|  |  robot.py.py                      # 早知道类模块
│                
├─discard_files                        # 废弃文件
|
│  README.md                           # 调用器介绍
│  robot_settings.py                   # 基础配置
|  mission_scheduler.py                # 早知道任务调度器
```

<br>

***

## 2、搭建流程

- 创建所需存储过程
- 修改robot_settings.py中基础配置
  - RESULT_DIR、MODEL_DIR 主路径
  - DATABASE_CON_INFOS：数据库连接串
- 在mission_scheduler.py中配置任务
  - SQL_dict：sql字典，每个key对应一个列表，列表内有2个值
    - key：存储过程名称
    - value:
      - list[0]为Excel模板中数据写入起始位置
      - list[1]为Excel模板中需清除数据区域
    - 写入流程：清除固定位置list[1]的数据，读取存储过程，从list[0]开始写入数据
  - PIC_dict：截图所需
    - key：早知道结果对应sheet名
    - value：需截图区域
  - API_dict：
    - key：早知道机器人URL
    - value：list，需传输的图片名称
  - file_name：早知道模板名称




可按上述流程简单写个测试一下，待流程跑通再进行开发