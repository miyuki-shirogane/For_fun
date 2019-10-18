#-*-coding:utf-8-*-

import requests,json,random,sys,ddt
import  unittest,time,os,datetime
import ExcelUtil
sys.path.append("../common")
import readDB_config
sys.path.append("../../config")
import config,testcase



#@ddt.ddt 在class前
#@ddt.data(*excel.next()) 在def前
#data['字段名'] 引用

def getHeaders():
    '''获取headers'''
    return {'accept':'application/json','Authorization':'Basic eWwuZkB0LmlvOjEyMzQ1Ng=='}


#这里获取到token就代表login成功，post接口不用再测；
def login():
    '''把token写入到文件中'''
    r = requests.post(
        url=config.address+config.login,
        json={"email":config.email,"password":config.password},
        headers=getHeaders())
    f = open(base_dir(),'w')
    f.write(r.json()['token'])

def base_dir():
    '''获取当前文件的目录'''
    return os.path.join(os.path.dirname(__file__), 'token.md')


def getToken():
    '''读取存储在文件中的token'''
    f = open(base_dir(),'r')
    return f.read()

#============================================================
def getHeaders1():
    '''获取headers'''
    return {'accept':'application/json','Authorization':'Basic YUB0LmlvOnRlbGV0cmFhbg=='}



def login1():
    '''把token写入到文件中'''
    r = requests.post(
        url=config.address+config.login,
        json={"email":config.email1,"password":config.password1},
        headers=getHeaders1())
    f = open(base_dir1(),'w')
    f.write(r.json()['token'])

def base_dir1():
    '''获取当前文件的目录'''
    return os.path.join(os.path.dirname(__file__), 'token1.md')


def getToken1():
    '''读取存储在文件中的token'''
    f = open(base_dir1(),'r')
    return f.read()

#============================================================
def getHeaders2():
    '''获取headers'''
    return {'accept':'application/json','Authorization':'Basic eWwuZi5qQHQuaW86MTIzNDU2'}



def login2():
    '''把token写入到文件中'''
    r = requests.post(
        url=config.address+config.login,
        json={"email":config.email2,"password":config.password2},
        headers=getHeaders2())
    f = open(base_dir2(),'w')
    f.write(r.json()['token'])

def base_dir2():
    '''获取当前文件的目录'''
    return os.path.join(os.path.dirname(__file__), 'token2.md')


def getToken2():
    '''读取存储在文件中的token'''
    f = open(base_dir2(),'r')
    return f.read()

#=========================================================================================

#字典叠加
def add_dict(d1,d2):
    result = d1.copy()
    result.update(d2)
    return result

#===========================================测试类======================================
class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.url=config.address

    def tearDown(self):
        time.sleep(1)
#--------------TestCase----------------
#------------------------------------------------------AUTH
#get me info_____GET
    def test_getmeinfo(self):
        '''验证：测试get me info接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.getmeinfo,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)
#------------------------------------------------------TAG
#tags仅list启用，其他都没开放；
#list tags_____GET
    def test_listtags(self):
        '''验证：测试list tag接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page}
        r = requests.get(url=self.url+config.listtags,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#--------------------------------------------------ORGANIZATION V2
#create organization_____POST
    def test_createorganization(self):
        '''验证：测试create organization接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"name":"test0","parent_id":'11',"person": "auto_person","email": "user@t.com","phone": "18","timezone": "UTC"}
        r = requests.post(url=self.url+config.createorganization,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)

#list organization_____GET
    def test_listorganization(self):
        '''验证：测试list organization接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page}
        r = requests.get(url=self.url+config.listorganization,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)


#retrieve organization_____GET
#case1
    def test_retrieveorganization_0(self):
        '''验证：测试retrieve organization接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrieveorganization_0,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#case2
    def test_retrieveorganization_1(self):
        '''验证：测试retrieve organization接口更high level是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrieveorganization_1,headers=headers,timeout=5)
        self.assertEqual(r.status_code,404)

#update organization_____PATCH
    def test_updateorganization(self):
        '''验证：测试update organization接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={"email":"user@e.com"}
        r = requests.patch(url=self.url+config.updateorganization,json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#delete organization_____DELETE
    def test_deleteorganization(self):
        '''验证：测试delete organization接口是否正确'''
        headers={'accept':'*/*',"Authorization":'Token '+getToken()}
        r = requests.delete(url=self.url+config.deleteorganization,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)

#deletable organization_____GET
    def test_deletebleorganization(self):
        '''验证：测试deleteable organization接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.deletableorganization,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["deletable"], False)

#get organization tree_____GET
#此处接口需求原文为：
#Get tree by current user：
#1.if user in level 1(root), return all orgs.
#2.if user in level 2(company), return company and departments orgs.
#3.if user in level 3(department), return company (but visible is false), and self department.
#为此设计如下三条用例：
#case1
    def test_getorganizationtree(self):
        '''验证：测试公司用户get organization tree接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.organizationtree,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)
        self.assertEqual(len(r.json()['descendants']),testcase.comnum)

#case2
    def test_getorganizationtree1(self):
        '''验证：测试root用户get organization tree接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken1()}
        r = requests.get(url=self.url+config.organizationtree,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)
        self.assertEqual(len(r.json()['descendants']),testcase.rootnum)

#case3
    def test_getorganizationtree2(self):
        '''验证：测试部门用户get organization tree接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken2()}
        r = requests.get(url=self.url+config.organizationtree,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)
        self.assertEqual(len(r.json()['descendants']),testcase.apartnum)








#----------------------------------------------------USER V2
#Create users_____POST
#case1
    def test_createusers(self):
        '''验证:发送空数据测试createusers返回是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"email":"","org_group":[4],"password": ""}
        r = requests.post(url=self.url+config.createusers,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,400)
        self.assertEqual(r.json()['errors']['email'][0]['code'],testcase.users_blank0)

#case2
    def test_createusers1(self):
        '''验证:发送重复数据测试createusers返回是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"email":"y@t.io","org_group":[4],"password": "string"}
        r = requests.post(url=self.url+config.createusers,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,400)
        self.assertEqual(r.json()['errors']['email'][0]['code'],testcase.users_unique0)

#case3
    def test_createusers2(self):
        '''验证:发送重复数据测试createusers返回是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"email":"auto_email"+str(random.randint(0,999))+"@t.io","org_groups": [
    4
  ],
  "password": "string"
}
        r = requests.post(url=self.url+config.createusers,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)


#list users_____GET
    def test_listusers(self):
        '''验证:测试listusers接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page,'organization':testcase.organization}
        r = requests.get(url=self.url+config.listusers,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#retrieve users_____GET
    def test_retrieveusers(self):
        '''验证:测试retrieveusers接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrieveusers,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#update users_____PATCH
    def test_updateusers(self):
        '''验证:测试updateusers接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={"username":"apartment"}
        r = requests.patch(url=self.url+config.updateusers,json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#delete users_____DELETE
    def test_deleteusers(self):
        '''验证：测试delete users接口是否正确'''
        headers={'accept':'*/*',"Authorization":'Token '+getToken()}
        r = requests.delete(url=self.url+config.deleteusers,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)



#-------------------------------------------DEVICE V2
#create device_____POST
    def test_createdevice(self):
        '''验证:测试create device接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"name": "auto_device"+str(random.randint(0,999)),"type": "android","org_groups": [4]}
        r = requests.post(url=self.url+config.createdevice,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)

#list  device_____GET
    def test_listdevice(self):
        '''验证:测试list device接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page}
        r = requests.get(url=self.url+config.listdevice,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#retrieve device_____GET
    def test_retrievedevice(self):
        '''验证:测试retrieve device接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrievedevice+str(readDB_config.select_device()[0])+"/",headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#update device_____PATCH
    def test_updatedevice(self):
        '''验证:测试updatedevice接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={"name":"auto_device777"}
        r = requests.patch(url=self.url+config.updatedevice+str(readDB_config.select_device()[0])+"/",json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#break
#这块比较特殊，原因是：device删除接口做的是软删除操作，即一个字段is_deleted标记是否删除；然后在删除过后，做其他get查询操作时，会把已经删去的记录也进行查询，
#导致404错误；那么这里以e为开头命名函数，让其在delete以后，再做一个硬删除操作，那么后面的get方法就不会报404了；
    def test_ele(self):
        '''不是接口不要在意'''
        readDB_config.delete_device_t()



#delete device_____DELETE
    def test_deletedevice(self):
        '''验证：测试delete device接口是否正确'''
        headers={'accept':'*/*',"Authorization":'Token '+getToken()}
        r = requests.delete(url=self.url+config.deletedevice,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)

#get device tag_____GET
    def test_gettagdevice(self):
        '''验证:测试retrieve device tag接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.gettagdevice+str(readDB_config.select_device()[0])+"/config/",headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#update device config_____POST
    def test_updatedeviceconfig(self):
        '''验证:测试update device config接口是否正确'''
        headers={'accept':'*/*','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data = {"ids": [str(readDB_config.select_device()[0])],"config": {"compare_count":str(random.randint(0,20))}}
        r = requests.post(url=self.url+config.updatedeviceconfig,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)

#get device config template_____GET
    def test_template(self):
        '''验证:测试get device config template接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.template,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)


#-----------------------------------------------------PERMISSION
#create permission_____POST
    def test_createpermission(self):
        '''验证:测试create permission接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"name":"auto_pms"+str(random.randint(0,999)),"organization_id":4,"access_time": [{"type": "time_period", "content": {"end": "23:59", "start": "00:00"}}]}
        r = requests.post(url=self.url+config.createpms,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)    

#create permission_____POST
    def test_createpermission_1(self):
        '''not case'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"name":"auto_pms"+str(random.randint(0,999)),"organization_id":4,"access_time": [{"type": "time_period", "content": {"end": "23:59", "start": "00:00"}}]}
        r = requests.post(url=self.url+config.createpms,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201) 


#delete permission_____DELETE
    def test_deletepermission(self):
        '''验证:测试delete permission接口是否正确'''
        headers={'accept':'*/*',"Authorization":'Token '+getToken()}
        r = requests.delete(url=self.url+config.deletepms,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)

#不用在意
    def test_elf(self):
        '''不是接口不要在意'''
        readDB_config.delete_permission_t()

#list permission_____GET
    def test_listpermission(self):
        '''验证:测试list permission接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page}
        r = requests.get(url=self.url+config.listpms,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#retrieve permission_____GET
    def test_retrievepms(self):
        '''验证:测试retrieve permission接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrievepms+str(readDB_config.select_pms())+"/",headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#update permission_____PATCH
    def test_updatepms(self):
        '''验证:测试updatepms接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={"name":"auto_pms777"}
        r = requests.patch(url=self.url+config.retrievepms+str(readDB_config.select_pms())+"/",json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)


#----------------------------------------------------MEMBER V2
#create member
#create member_____POST
#case1
    def test_createmember0(self):
        '''验证:测试create permission接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"name":"auto_member"+str(random.randint(10000,99999)),"serial_number":str(random.randint(0,9999)),"organization_id": 4,"department": "auto_department"+str(random.randint(0,999)),"job_level": "auto_joblevel"+str(random.randint(0,999))}
        r = requests.post(url=self.url+config.createmember,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201) 

#case2
    def test_createmember1(self):
        '''验证:测试create permission接口输入重复人员id是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"name":"auto_member"+str(random.randint(10000,99999)),"serial_number":str(readDB_config.select_mem()[0]),"organization_id": 4,"department": "auto_department"+str(random.randint(0,999)),"job_level": "auto_joblevel"+str(random.randint(0,999))}
        r = requests.post(url=self.url+config.createmember,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,400) 

#not case；为后面批量删除做准备
    def test_createmember2(self):
        '''不是接口，不要在意'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"name":"auto_member"+str(random.randint(10000,99999)),"serial_number":str(random.randint(0,9999)),"organization_id": 4,"department": "auto_department"+str(random.randint(0,999)),"job_level": "auto_joblevel"+str(random.randint(0,999))}
        r = requests.post(url=self.url+config.createmember,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201) 

#not case；
    def test_a(self):
        '''不是接口，不要在意'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"name":"misaka","serial_number":str(random.randint(0,9999)),"organization_id": 4,"department": "d","job_level": "j"}
        r = requests.post(url=self.url+config.createmember,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201) 

#delete member_____DELETE
    def test_deletemember(self):
        '''验证:测试delete member接口是否正确'''
        headers={'accept':'*/*',"Authorization":'Token '+getToken()}
        r = requests.delete(url=self.url+config.deletemember,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)

#batch delete member_____POST
    def test_deletemember_b(self):
        '''验证:测试batch delete member接口是否正确'''
        headers={'accept':'*/*','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"ids": [readDB_config.select_mem()[1]]}
        r = requests.post(url=self.url+config.batchdeletemember,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)

#不用在意
    def test_elg(self):
        '''不是接口不要在意'''
        readDB_config.delete_member_t()

#update member_____PATCH
    def test_updatemember(self):
        '''验证:测试update member接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={"name":"auto_member2333"}
        r = requests.patch(url=self.url+config.updatemember+str(readDB_config.select_mem()[1])+"/",json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#batch update member_____POST
    def test_updatemember_b(self):
        '''验证:测试batch update member接口是否正确'''
        headers={'accept':'*/*','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"ids": [readDB_config.select_mem()[1]], "fields":{"permissions": [readDB_config.select_pms()]}}
        r = requests.post(url=self.url+config.batchupdatemember,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)

#list member_____GET
    def test_listmembers(self):
        '''验证:测试list member接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page}
        r = requests.get(url=self.url+config.listmember,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)



#retrieve member_____GET
    def test_retrievemembers(self):
        '''验证:测试retrieve member接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrievemember+str(readDB_config.select_mem()[1])+"/",headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#--------------------------------------------------MEMBER RECORD
#create member record
    def test_create_mrecord(self):
        '''验证:测试create member record接口是否正确'''
        headers={'accept':'*/*','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"device_uuid":str(readDB_config.select_device()[1]),"type":-1,"start":1555257600000,"end":1555308325000}
        r = requests.post(url=self.url+config.createmr,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)

#get member record
    def test_list_mrecord(self):
        '''验证:测试list member record接口是否正确,以及返回查询结果是否符合提取条件'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page,'start':1557936402000,'end':1557972402000}
        r = requests.get(url=self.url+config.listmr,params=params,headers=headers,timeout=5)
        n = len(r.json())
        a = 0
        list = []
        list1 = []
        list_s = []
        while a<n:
            list.append(r.json()[a]['start'])
            a=a+1
        for time in list:
            if time >= 1557936402000 and time <= 1557972402000:
                list_s.append(1)
            else:
                list_s.append(0)
        s=1
        for i in list_s:
            s*=i
        self.assertEqual(r.status_code,200)
        self.assertEqual(s,1)

#update member record
    def test_update_mrecord(self):
        '''验证:测试update member record接口是否正确'''
        headers={'accept':'*/*','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={
  "video": {
    "id": readDB_config.select_video_id(),
    "src": "https://example.com/videos/123"
  }
}
        r = requests.patch(url=self.url+config.updatemr+str(readDB_config.select_mrid())+"/",json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)



#---------------------------------------------------VEHICLE
#create vehicle_____POST
#case1
    def test_createvehicle(self):
        '''验证:测试create vehicle接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"license_plate": "浙A"+str(random.randint(10000,99999)),"owner": "auto_owner"+str(random.randint(100,999)),"organization_id":4}
        r = requests.post(url=self.url+config.createvehicle,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)

#case2
    def test_createvehicle1(self):
        '''验证:测试create vehicle接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"license_plate":"浙"+readDB_config.select_vehicle()[1],"owner": "auto_owner"+str(random.randint(100,999)),"organization_id":4}
        r = requests.post(url=self.url+config.createvehicle,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,400) 

#case3
    def test_createvehicle2(self):
        '''前面测过了，不要在意'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"license_plate": "浙A"+str(random.randint(10000,99999)),"owner": "auto_owner"+str(random.randint(100,999)),"organization_id":4}
        r = requests.post(url=self.url+config.createvehicle,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)


#delete vehicle_____DELETE
    def test_deletevehicle(self):
        '''验证:测试delete vehicle接口是否正确'''
        headers={'accept':'*/*',"Authorization":'Token '+getToken()}
        r = requests.delete(url=self.url+config.deletevehicle,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)

#不用在意
    def test_elh(self):
        '''不是接口不要在意'''
        readDB_config.delete_vehicle_t()

#list vehicle_____GET
    def test_listvehicle(self):
        '''验证:测试list vehicle接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page}
        r = requests.get(url=self.url+config.listvehicle,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#retrieve vehicle_____GET
    def test_retrievevehicle(self):
        '''验证:测试retrieve vehicle接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrievevehicle+str(readDB_config.select_vehicle()[0])+"/",headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#update vehicle_____PATCH
    def test_updatevehicle(self):
        '''验证:测试update vehicle接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={"owner":"auto_owner777"}
        r = requests.patch(url=self.url+config.retrievevehicle+str(readDB_config.select_vehicle()[0])+"/",json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)




#--------------------------------------------------VEHICLE RECORD
#create vehicle record
    def test_create_vrecord(self):
        '''验证:测试create member record接口是否正确'''
        headers={'accept':'*/*','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"device_uuid":str(readDB_config.select_device()[1]),"type":-1,"start":1555257600000,"end":1555308325000}
        r = requests.post(url=self.url+config.createvr,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)

#get vehicle record
    def test_list_vrecord(self):
        '''验证:测试list vehicle record接口是否正确,以及返回查询结果是否符合提取条件'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page,'start':1557072677000,'end':1555308325000}
        r = requests.get(url=self.url+config.listvrecord,params=params,headers=headers,timeout=5)
        n = len(r.json())
        a = 0
        list = []
        list_s = []
        while a<n:
            list.append(r.json()[a]['start'])
            a=a+1
        for time in list:
            if time >= 1557072677000 and time <= 1555308325000:
                list_s.append(1)
            else:
                list_s.append(0)
        s=1
        for i in list_s:
            s*=i
        self.assertEqual(r.status_code,200)
        self.assertEqual(s,1)

#update vehicle record
    def test_update_vrecord(self):
        '''验证:测试update vehicle record接口是否正确'''
        headers={'accept':'*/*','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={
  "video": {
    "id": readDB_config.select_video_id(),
    "src": "https://example.com/videos/123"
  }
}
        r = requests.patch(url=self.url+config.updatevr+str(readDB_config.select_vrid())+"/",json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)





#----------------------------------------------VISITOR
#create event + visitor
    def test_fcreate_ev(self):
        '''验证:测试create event + visitor接口是否正确'''
        n = datetime.datetime.now()+datetime.timedelta(days=3)
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data = {"action": "invite",
        "event": {"target": "auto_target"+str(random.randint(100,999)),"organization_id": 4,
        "access_time": [{"date":str(n.strftime("%Y-%m-%d")),"start": "09:00","end": "18:00","leave": "19:00"}],
        "permissions": [readDB_config.select_pms()]},
        "visitors": [{"name": "auto_visitor"+str(random.randint(100,999)),"phone": "1382424"+str(random.randint(1000,9999))}]}
        r = requests.post(url=self.url+config.createev,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)

#batch create visitor
    def test_fcreate_v(self):
        '''验证:测试 在event 下批量create visitor接口是否正确'''
        headers={'accept':'*/*','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"event":readDB_config.select_event()[0],"action":"invite",
        "visitors":[{"name":"auto_visitor"+str(random.randint(100,999)),"phone":"1382424"+str(random.randint(1000,9999))},
        {"name":"auto_visitor"+str(random.randint(100,999)),"phone":"1382424"+str(random.randint(1000,9999))}]}
        r = requests.post(url=self.url+config.createv,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)

#create regular visitor
    def test_create_rv(self):
        '''验证:测试 create regular visitor接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"name": "auto_rv"+str(random.randint(100,999)),"phone": "1567272"+str(random.randint(1000,9999)),"organization_id": 4}
        r = requests.post(url=self.url+config.createrv,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)

#create regular visitor
    def test_create_rv(self):
        '''not case'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"name": "auto_rv"+str(random.randint(100,999)),"phone": "1567272"+str(random.randint(1000,9999)),"organization_id": 4}
        r = requests.post(url=self.url+config.createrv,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)

#delete regular visitor
    # def test_delete_rv(self):
    #     '''验证:测试 delete regular visitor接口是否正确'''
    #     headers={'accept':'*/*',"Authorization":'Token '+getToken()}
    #     r = requests.delete(url=self.url+config.deleterv,headers=headers,timeout=5)
    #     self.assertEqual(r.status_code,204)

#list event
    def test_listevent(self):
        '''验证:测试list event接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.listevent,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#retrieve event_____GET
    def test_retrieveevent(self):
        '''验证:测试retrieve event接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrieveevent+str(readDB_config.select_event()[0])+"/",headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#update event_____PATCH
    def test_updateevent(self):
        '''验证:测试update event接口是否正确'''
        m = datetime.datetime.now()+datetime.timedelta(days=4)
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={"action":"update","data":{"target": "auto_target"+str(random.randint(100,999)),"access_time":[{"date":str(m.strftime("%Y-%m-%d")),"start": "10:00","end": "19:00","leave": "22:00"}]}}
        r = requests.patch(url=self.url+config.updateevent+str(readDB_config.select_event()[0])+"/",json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#batch update visitor
    def test_updatevb(self):
        '''验证:测试batch update visitor接口是否正确'''
        headers={'accept':'*/*','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"ids":[readDB_config.select_v()],"action":"audit"}
        r = requests.post(url=self.url+config.updatevb,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)

#retrieve visitor_____GET
    def test_retrievev(self):
        '''验证:测试retrieve visitor接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrievev+str(readDB_config.select_v())+"/",headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#update visitor_____PATCH
    def test_updatev(self):
        '''验证:测试update visitor接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={"action": "invite","data": {"phone":"1567272"+str(random.randint(1000,9999)),"allow_add":'true',"is_frequent":'true'}}
        r = requests.patch(url=self.url+config.updatev+str(readDB_config.select_v())+"/",json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)



#list regular visitor
    def test_listrv(self):
        '''验证:测试list regular visitor接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page}
        r = requests.get(url=self.url+config.listrv,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#retrieve rv_____GET
    def test_retrieverv(self):
        '''验证:测试retrieve rv接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrieverv+str(readDB_config.select_rv())+"/",headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#update rv_____PATCH
    def test_updaterv(self):
        '''验证:测试update rv接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={"phone":"1567272"+str(random.randint(1000,9999))}
        r = requests.patch(url=self.url+config.updaterv+str(readDB_config.select_rv())+"/",json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)


#------------------------------------------ATTENDANCE
#create holiday_____POST
    def test_createholiday(self):
        '''验证:测试create holiday接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"name": "auto_holiday"+str(random.randint(100,999)),"start_on": "2029-09-01","end_on": "2029-09-05",
        "detail": {
        "holidays": [str(random.randint(2025,2090))+"-09-01"]
        }
        }
        r = requests.post(url=self.url+config.createholiday,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)

#list holidays_____GET
    def test_listholiday(self):
        '''验证:测试list holiday接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page}
        r = requests.get(url=self.url+config.listholiday,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#retrieve holidays_____GET
    def test_retrieveholiday(self):
        '''验证:测试retrieve holiday接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrieveholiday+str(readDB_config.select_holiday())+"/",headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#update holiday_____PATCH
    def test_updateholiday(self):
        '''验证:测试update holiday接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={"name":"auto_holiday"+str(random.randint(100,999))}
        r = requests.patch(url=self.url+config.updateholiday+str(readDB_config.select_holiday())+"/",json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#delete holiday_____DELATE
    def test_ydeleteholiday(self):
        '''验证:测试delete holiday接口是否正确'''
        headers={'accept':'*/*',"Authorization":'Token '+getToken()}
        r = requests.delete(url=self.url+config.deleteholiday+str(readDB_config.select_holiday())+"/",headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)

#set overtimeratio_____POST
    def test_createovertimeratio(self):
        '''验证:测试set overtimeratio接口是否正确'''
        headers={'accept':'*/*','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        data={"holiday":5,"off_day":3,"working_day":2,"welfare":4,"organization_id":4}
        r = requests.post(url=self.url+config.setovertimeratio,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,204)

#get overtimeratio_____GET
    def test_getovertimeratio(self):
        '''验证:测试get overtime ratio接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.getovertimeratio,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#create shift_____POST
    def test_createshift(self):
        '''验证:测试create shift接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
#例外规则参数没有添加，接口文档貌似有问题，抛400；detail:"message": "Must be a ExceptiveRule type json, ExceptiveRule: expected string or bytes-like object","code": "invalid"
        data = {
  "name": "auto_shift"+str(random.randint(100,999)),
  "apply_to": {
    "d": [
      "j"]
  },
  "working_days": [
    1,
    2,
    3,
    4,
    5
  ],
  "auto_holiday": 'true',
  "punch_time": {
    "name": "auto_punchtime"+str(random.randint(100,999)),
    "type": "fixed",
    "rule": {
      "periods": [
        {
          "on_duty_at": "01:00",
          "off_duty_at": "09:00",
          "on_duty_range": {
            "start": {
              "type": "before",
              "time": "23:00"
            },
            "end": {
              "type": "on",
              "time": "03:00"
            }
          },
          "off_duty_range": {
            "start": {
              "type": "on",
              "time": "08:00"
            },
            "end": {
              "type": "on",
              "time": "10:00"
            }
          }
        }
      ],
      "late_after": 30,
      "leave_early_before": 30,
      "absent": {
        "late": {
          "threshold": 150,
          "value": 0.5
        },
        "leave_early": {
          "threshold": 150,
          "value": 0.5
        },
        "no_on_duty": 0.5,
        "no_off_duty": 0.5
      },
      "enable_overtime": 'true',
      "overtime_rule": {
        "min_unit": 30,
        "enable_on_duty": 'true',
        "before_on_duty": 60,
        "enable_off_duty": "ture",
        "after_off_duty": 60
      }
    }
  }
}
        r = requests.post(url=self.url+config.createshift,json=data,headers=headers,timeout=5)
        self.assertEqual(r.status_code,201)

#delete shift_____DELETE
    # def test_deleteshift(self):
        # '''验证:测试delete shift接口是否正确'''
        # headers={'accept':'*/*',"Authorization":'Token '+getToken()}
        # r = requests.delete(url=self.url+config.deleteshift+str(readDB_config.select_shift())+"/",headers=headers,timeout=5)
        # self.assertEqual(r.status_code,204)

#update shift_____PATCH
    def test_updateshift(self):
        '''验证:测试update shift接口是否正确'''
        headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
        paramdata={"name":"auto_shift"+str(random.randint(100,999))}
        r = requests.patch(url=self.url+config.updateshift+str(readDB_config.select_shift())+"/",json=paramdata,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#list shift_____GET
    def test_listshift(self):
        '''验证:测试list shift接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page}
        r = requests.get(url=self.url+config.listshift,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#retrieve shift_____GET
    def test_retrieveshift(self):
        '''验证:测试retrieve shift接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrieveshift+str(readDB_config.select_shift())+"/",headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#list punch time_____GET
    def test_listpunchtime(self):
        '''验证:测试list punchtime接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page}
        r = requests.get(url=self.url+config.listpunchtime,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#retrieve punch time_____GET
    def test_retrievepunchtime(self):
        '''验证:测试retrieve punchtime接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.retrievepunchtime+str(readDB_config.select_punchtime())+"/",headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)



    def test_z(self):
        '''删除misaka仿生人'''
        readDB_config.delete_misaka()

#list monthly report_____GET
    def test_listmonthlyreport(self):
        '''验证:测试list monthly report接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'month':'2019-06','departments':'d','name':'misaka'}
        r = requests.get(url=self.url+config.listmonthlyreport,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#export monthly report_____GET
    def test_exportmr(self):
        '''验证:测试export monthly report接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'month':'2019-06','departments':'d','name':'misaka'}
        r = requests.get(url=self.url+config.exportmonthlyreport,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#list daily report_____GET
    def test_listdailyreport(self):
        '''验证:测试list daily report接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'month':'2019-06','departments':'d','name':'misaka'}
        r = requests.get(url=self.url+config.listdailyreport,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#export daily report_____GET
    def test_exportdr(self):
        '''验证:测试export daily report接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        params={'month':'2019-06','departments':'d','name':'misaka'}
        r = requests.get(url=self.url+config.exportdailyreport,params=params,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#list dpartment with job levels_____GET
    def test_listdj(self):
        '''验证:测试list dj接口是否正确'''
        headers={'accept':'application/json',"Authorization":'Token '+getToken()}
        r = requests.get(url=self.url+config.listdj,headers=headers,timeout=5)
        self.assertEqual(r.status_code,200)

#update daily report_____PATCH
    # def test_updatedr(self):
    #     headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token '+getToken()}
    #     paramdata={}
    #     r = requests.patch(url=self.url+config.updatedr+str(readDB_config.select_dr())+"/",json=paramdata,headers=headers,timeout=5)
    #     self.assertEqual(r.status_code,200)

if __name__ == '__main__':
    #test_data.init_data() # 初始化接口测试数据

    login()
    login1()
    login2()
    unittest.main(verbosity=2)


