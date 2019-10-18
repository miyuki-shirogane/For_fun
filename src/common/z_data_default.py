# coding:utf-8
 
from z_sql_act import DB
# 创建测试数据
datas = {
    # tags_tag表数据
    "tags_tag":[
        {"id":1,"name":"test_membertag","type":"member","organization_id":4},
        {"id":2,"name":"test_devicetag","type":"device","organization_id":4},
        {"id":3,"name":"test_vehicletag","type":"vehicle","organization_id":4}
    ]
}
 
# 将测试数据插入表
def init_data():
    db = DB()
    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table,d)
    db.close()
 
if __name__ == '__main__':
    init_data()
