#coding:utf-8
 
import os
import psycopg2
import configparser

# ================读取db_config.ini文件设置=================
 
 
root_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
configPath = os.path.join(root_path,"config/db_config.ini")
cf = configparser.ConfigParser()
cf.read(configPath,encoding='UTF-8')

host = cf.get("postgresqlconf","host")
port = cf.get("postgresqlconf","port")
db = cf.get("postgresqlconf","db")
user = cf.get("postgresqlconf","user")
password = cf.get("postgresqlconf","password")

# ================封装MySQL基本操作=================
class DB:
    def __init__(self):
        #连接测试数据库
        self.conn = psycopg2.connect(host = host,
            port = port,
            user = user,
            password = password,
            dbname = db)
 

 #暂时让表外键约束失效方法暂未找到；tags_tag表暂无这种困扰，故可以直接执行成功；
    # 清除表数据
    def clear(self,tabel_name):
        real_sql = "truncate table "+ tabel_name +" cascade;"
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()
 
    # 插入表数据
    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ",".join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value +")" + ";"
        print(real_sql)
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

        
 
#     # 关闭数据库连接
    def close(self):
        self.conn.close()
 
if __name__ == '__main__':
    db = DB()
    table_name0 = "organizations_organization"
    column_name0 = 'id'
    db.select(table_name0,column_name0)
    db.close()
    data = {"id":1,
            "name":"test_tag",
            "type":"member",
            "organization_id":4
            }
    db.clear(table_name)
    db.insert(table_name,data)
