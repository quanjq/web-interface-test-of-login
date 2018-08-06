# -*-encoding:utf-8 -*-
from pymysql import connect,cursors
from pymysql.err import OperationalError
import sys
sys.path.append('../db_fixture')



# 需要连接的数据库的基本配置信息
host ='10.1.20.85'
port =3306
user =u'root'
password =u'root'
db_name =u'guest'

class DB:
    def __init__(self):
        '''u初始化，连接数据库'''
        try:
             self.conn = connect(host=host,
                                port=port,
                                user=user,
                                password=password,
                                db=db_name,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor)
             #print('start')
        except OperationalError as e:
            print('mysql error : %d: %s' %(e.args[0],e.args[1]))
    def clear_bd(self,table_name):
        '''u清除某张表，清除之前，需要将外键删除'''
        clear_sql ='delete from '+ table_name +';'
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(clear_sql)
        self.conn.commit()

    def insert_db(self,table_name,table_data):
        '''u插入数据库'''
        for key in table_data:
            table_data[key] ="'"+str(table_data[key])+"'"
        key =",".join(table_data.keys())
        value =",".join(table_data.values())
        insert_sql ='insert into '+table_name+"("+key+")values ("+ value +");"
        print insert_sql
        with self.conn.cursor() as cursor:
            cursor.execute(insert_sql)
        self.conn.commit()


    def select_bd(self,table_name,conditions):
        '''u查询数据库'''
        select_sql='select * from '+table_name+" "+conditions+" ;"
        with self.conn.cursor() as cursor:
            cursor.execute(select_sql)
            select_result=cursor.fetchall()
        return select_result

    def close_bd(self):
        '''u关闭数据库'''
        self.conn.close()


if __name__ == '__main__':
        db = DB()
        db.close_bd()
        #print ('end')
