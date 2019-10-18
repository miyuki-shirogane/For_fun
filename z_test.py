#-*-coding:utf-8-*-

import requests
import random,config.testcase,config.config
import time,datetime


# def login():
#     '''把token写入到文件中'''
#     r = requests.post(
#         url=config.address+config.login,
#         json={"email":config.email,"password":config.password},
#         headers={'accept':'application/json','Authorization':'Basic eWwuZkB0LmlvOjEyMzQ1Ng=='})
#     print r.json()['token']


def t():
	# headers={'accept':'application/json','Content-Type':'application/json',"Authorization":'Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjA1Nzg3MzksInVzZXIiOnsiaWQiOjUsImVtYWlsIjoieWwuZkB0LmlvIn19.U-Bi3SSsJWSrDVXq07eYC-S5DRQq7AuIVXkKtTTWM5o'}
	headers={'accept':'application/json',"Authorization":'Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjMyNTAyNTMsInVzZXIiOnsiaWQiOjUsImVtYWlsIjoieWwuZkB0LmlvIn19.aEbu_fU1Kb0a5T1eLhtPoKYBPl9lFUg4P92yg0iv3qY'}
	params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page}
	r = requests.get(url=config.address+config.listmr,params=params,headers=headers,timeout=5)
	print r.status_code



        # data = {"action": "invite",
        # "event": {"target": "auto_target"+str(random.randint(100,999)),"organization_id": 4,
        # "access_time": [{"date":str(n.strftime("%Y-%m-%d")),"start": "09:00","end": "18:00","leave": "19:00"}],
        # "permissions": [readDB_config.select_pms()]},
        # "visitors": [{"name": "auto_visitor"+str(random.randint(100,999)),"phone": "1382424"+str(random.randint(1000,9999))}]}
        # r = requests.post(url=config.address+config.createev,json=data,headers=headers,timeout=5)
        # print r.raw
	# params={'page':testcase.page,'page_size':testcase.page_size,'no_page':testcase.no_page,'start':1557072677000,'end':1555308325000}
	# r = requests.get(url=config.address+config.createmr,params=params,headers=headers,timeout=5)
	# n = len(r.json())
	# a = 0
	# list = []
	# list_s = []
	# while a<n:
	# 	list.append(r.json()[a]['start'])
	# 	a=a+1
	# for time in list:
	# 	if time >= 1544153985349 and time <= 1557972402000:
	# 		list_s.append(1)
	# 	else:
	# 		list_s.append(0)
	# s=1
	# for i in list_s:
	# 	s*=i
	# print s
	# print list_s.  time.strftime("%Y-%m-%d")


	# n = datetime.datetime.now()+datetime.timedelta(days=3)
	# print str(n.strftime("%Y-%m-%d"))





if __name__ == '__main__':
	# readDB_config.select()
	t()


#--------0508的token: test ok




# if start > xxxx and start <xxxx:
# 	r = 1
# else:
# 	r=0
# 	self.assertequal(r,1)
