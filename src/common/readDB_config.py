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

def select_org():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    table_name0 = "organizations_organization"
    column_name0 = 'id'

    real_sql = "select "+column_name0+' from '+ table_name0 +" where person like 'auto%';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result[0]

#===============================================================================================================

def select_users():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    table_name1 = "users_user"
    column_name1 = 'id'

    real_sql = "select "+column_name1+' from '+ table_name1 +" where email like 'auto%';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result[0]

#===============================================================================================================

def select_device():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    table_name2 = "devices_device"
    column_name2 = 'id'
    column_name2_1 = 'uuid'

    real_sql = "select "+column_name2+','+column_name2_1+' from '+ table_name2 +" where name like 'auto%' and is_deleted = 'f';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result

def delete_device_t():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)
    real_sql = ("delete from devices_device_org_groups where device_id in (select id from devices_device where is_deleted = 't');"
        "delete from memberrecords_memberrecord where device_id in (select id from devices_device where is_deleted = 't');"
        "delete from vehiclerecords_vehiclerecord where device_id in (select id from devices_device where is_deleted = 't');"
        "delete from devices_device where is_deleted = 't';")
    cursor = conn.cursor()
    cursor.execute(real_sql)
    conn.commit()

#===============================================================================================================

def select_pms():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    table_name3 = "accesscontrol_permission"
    column_name3 = 'id'

    real_sql = "select "+column_name3+' from '+ table_name3 +" where name like 'auto%' and is_deleted = 'f';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result[0]

def delete_permission_t():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)
    real_sql = "delete from members_member_permissions where permission_id in (select id from accesscontrol_permission where is_deleted = 't' and name like 'auto%');"
    "delete from visitors_event_permissions where permission_id in (select id from accesscontrol_permission where is_deleted = 't' and name like 'auto%')"
    "delete from accesscontrol_permission where is_deleted = 't' and name like 'auto%';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    conn.commit()

#===============================================================================================================

def select_mem():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    table_name4 = "members_member"
    column_name4 = 'serial_number'
    column_name4_1 = 'id'

    real_sql = "select "+column_name4+','+column_name4_1+' from '+ table_name4 +" where name like 'auto%' and is_deleted = 'f';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result


def delete_member_t():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)
    real_sql = "delete from members_member_permissions where member_id in (select id from members_member where is_deleted = 't' and name like 'auto%');delete from members_member where is_deleted = 't' and name like 'auto%';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    conn.commit()

#===============================================================================================================


def select_vehicle():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    table_name5 = "vehicles_vehicle"
    column_name5 = 'id'
    column_name5_1 = 'license_plate'

    real_sql = "select "+column_name5+',right('+column_name5_1+',6) from '+ table_name5 +" where owner like 'auto%' and is_deleted = 'f';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result

def delete_vehicle_t():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)
    real_sql = "delete from vehicles_vehicle where is_deleted = 't' and owner like 'auto%';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    conn.commit()

#===============================================================================================================
#MEMBER/VEHICLE RECORD 和VIDEO FILE的一个联动；处理逻辑是随机抽取一个video id 赋给最小的member record
def select_video_id():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    table_name6 = "files_video"
    column_name6 = 'id'

    real_sql = "select "+column_name6+' from '+ table_name6 +";"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result[0]

def select_mrid():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    real_sql = 'select id from memberrecords_memberrecord where id = (select min(id) from memberrecords_memberrecord);'
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result[0]   

def select_vrid():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    real_sql = 'select id from vehiclerecords_vehiclerecord where id = (select min(id) from vehiclerecords_vehiclerecord);'
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result[0]






#===============================================================================================================
def select_event():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    real_sql = "select id,target from visitors_event where target like 'auto%';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result  

def select_rv():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    real_sql = "select id from visitors_frequenter where name like 'auto%';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result[0] 

def select_v():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    real_sql = "select id from visitors_visitor where name like 'auto%';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result[0] 

def select_holiday():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    real_sql = "select id from attendances_holiday where name like 'auto%';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result[0] 

def select_shift():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    real_sql = "select id from attendances_shift where name like 'auto%';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result[0] 

def select_punchtime():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    real_sql = "select id from attendances_punchtime where name like 'auto%';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result[0] 

def insert_misaka():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)
    real_sql = "INSERT INTO members_member (name,organization_id,department,job_level) VALUES ('misaka',4,'d','j');"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    conn.commit()

def delete_misaka():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)
    real_sql = "delete from members_member where name = 'misaka';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    conn.commit()

def select_dr():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    real_sql = "select id from attendances_dailyattendance where name = 'misaka';"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchone()
    return result[0] 





def d():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)

    real_sql = "delete from memberrecords_memberrecord where id in (select id from memberrecords_memberrecord where device_id = '32' limit 10000);"
    # real_sql = "alter table attendances_holiday drop all_dates"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    conn.commit()

def s():
    conn = psycopg2.connect(host = host,
        port = port,
        user = user,
        password = password,
        dbname = db)


    real_sql = "select 28300*103"

    # real_sql = "select id from attendances_shift where name like 'auto%';"
    # real_sql = "select shifts from attendances_dailyattendance where member_id = (select id from members_member where name = 'C');"
    cursor = conn.cursor()
    cursor.execute(real_sql)
    result=cursor.fetchall()
    print result[0]

if __name__ == '__main__':
    s()


# members_member:{    department:a,job_level:b      }
# attendances_shift:{    apply_to:{u'A': [u'B']}      }




