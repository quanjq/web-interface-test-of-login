# -*-encoding:utf-8 -*-
import  time

from mysql_bd import DB


now_time=time.strftime( '%Y-%m-%d %X', time.localtime(time.time()) )
future_time=time.strftime( '%Y-%m-%d %X', time.localtime(time.time()+2592000) )
past_time=time.strftime( '%Y-%m-%d %X', time.localtime(time.time()-2592000) )

datas={
    #发布会数据
    'sign_event':[
        {'id':1,'name':'红米Pro发布会','`limit`':2000,'status':1,'address':'北京会展中心','start_time':future_time,'create_time':now_time},
        {'id':2,'name':'可参加人数为0','`limit`':0,'status':1,'address':'北京会展中心','start_time':future_time,'create_time':now_time},
        {'id':3,'name':'当前状态为0关闭','`limit`':2000,'status':0,'address':'北京会展中心','start_time':future_time,'create_time':now_time},
        {'id':4,'name':'发布会已结束','`limit`':2000,'status':1,'address':'北京会展中心','start_time':past_time,'create_time':now_time},
        {'id':5,'name':'小米5发布会','`limit`':2000,'status':1,'address':'北京国家会议中心','start_time':future_time,'create_time':now_time},
    ],
    #嘉宾数据
    'sign_guest':[
        {'id':1,'realname':'alen','phone':13511001100,'email':'alen@mail.com','sign':0,'event_id':1,'create_time':now_time},
        {'id':2,'realname':'has sign','phone':13511001101,'email':'sign@mail.com','sign':1,'event_id':1,'create_time':now_time},
        {'id':3,'realname':'tom','phone':13511001102,'email':'tom@mail.com','sign':0,'event_id':5,'create_time':now_time},
    ]
}

def init_data():
    db=DB()
    for table,data in datas.items():
        db.clear_bd(table)
        for d in data:
            db.insert_db(table,d)
    db.close_bd()
if __name__=='__main__':
    init_data()
    print(u'整体执行')
