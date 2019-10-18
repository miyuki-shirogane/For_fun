#coding=utf-8
#api文档地址：http://192.168.1.5:2016/swagger/#/
import testcase
import sys
sys.path.append("src/common")
import readDB_config






#登录信息
address = 'http://192.168.1.5:2016'
email = 'yl.f@t.io'
password = '123456'
email1 = 'a@t.io'
password1 = 'teletraan'
email2 = 'yl.f.j@t.io'
password2 = '123456'

#接口地址

login = '/auth/login/'

#AUTH
#get me info
getmeinfo = '/auth/me/'

#TAG
#create tag
createtag = '/api/v1/tags/'
#list tags
listtags = '/api/v1/tags/'

#ORGANIZATION
#create organization
createorganization = '/api/v2/organizations/'

#list organization
listorganization = '/api/v2/organizations/'

#retrieve organization
retrieveorganization_0 = '/api/v2/organizations/'+testcase.oid_0+'/'

retrieveorganization_1 = '/api/v2/organizations/'+testcase.oid_1+'/'

#update organization
updateorganization = '/api/v2/organizations/'+testcase.oid_2+'/'

#delete organization
deleteorganization = "/api/v2/organizations/"+str(readDB_config.select_org())+"/"

#其他get
deletableorganization = '/api/v2/organizations/'+testcase.oid_3+'/deletable/'

organizationtree = '/api/v2/organizations/tree/'




#USER_V2
#create users
createusers = '/api/v2/users/'

#get uesrs
listusers = '/api/v2/users/'

#其他get
retrieveusers = '/api/v2/users/'+testcase.uid_0+'/'

#update users
updateusers = '/api/v2/users/'+testcase.uid_0+'/'

#delete users
deleteusers = "/api/v2/users/"+str(readDB_config.select_users())+"/"



#DEVICE V2
#create device
createdevice = "/api/v2/devices/"

#list device
listdevice = "/api/v2/devices/"

#retrieve device
retrievedevice = "/api/v2/devices/"

#update device
updatedevice = "/api/v2/devices/"

#delete device
deletedevice = "/api/v2/devices/"+str(readDB_config.select_device()[0])+"/"

#get device tag
gettagdevice = "/api/v2/devices/"

#update device config
updatedeviceconfig = '/api/v2/devices/update-config/'

template = '/api/v2/device-config-templates/android/'



#PERMISSION
#create permission
createpms = '/api/v1/permissions/'

#delete permission
deletepms = '/api/v1/permissions/'+str(readDB_config.select_pms())+"/"

#list permission
listpms = '/api/v1/permissions/'

#retrieve permission
retrievepms = '/api/v1/permissions/'







#MEMBER
#create member
createmember = '/api/v2/members/'

#delete member
deletemember = '/api/v2/members/'+str(readDB_config.select_mem()[1])+"/"

#batch delete member
batchdeletemember = '/api/v2/members/batch-delete/'

#update member
updatemember = '/api/v2/members/'

#batch update member
batchupdatemember = '/api/v2/members/batch-update/'

#list member
listmember = '/api/v2/members/'

#retrieve member
retrievemember = '/api/v2/members/'





#MEMBER RECORD
#create member record
createmr = '/api/v1/member-records/'

#list member record
listmr = '/api/v1/member-records/'

#update member record
updatemr = '/api/v1/member-records/'






#VEHICLE
#create vehicle
createvehicle = '/api/v1/vehicles/'

#delete vehicle
deletevehicle = '/api/v1/vehicles/'+str(readDB_config.select_vehicle()[0])+"/"

#list vehicle
listvehicle = '/api/v1/vehicles/'

#retrieve vehicle
retrievevehicle = '/api/v1/vehicles/'


#VEHICLE RECORD
#create vehicle record
createvr = '/api/v1/vehicle-records/'

#list vehicle record
listvrecord = '/api/v1/vehicle-records/'

updatevr = '/api/v1/vehicle-records/'





#VISOTOR V2
createev = '/api/v2/visit-events/'

createv = '/api/v2/visitors/batch-create/'

createrv = '/api/v2/frequenters/'

#deleterv = '/api/v2/frequenters/'+str(readDB_config.select_rv())+'/'

listevent = '/api/v2/visit-events/'

retrieveevent = '/api/v2/visit-events/'

updateevent = '/api/v2/visit-events/'

updatevb = '/api/v2/visitors/batch-update/'

retrievev = '/api/v2/visitors/'

updatev = '/api/v2/visitors/'

listrv = '/api/v2/frequenters/'

retrieverv = '/api/v2/frequenters/'

updaterv = '/api/v2/frequenters/'


#ATTENDANCE V2
createholiday = '/api/v2/holidays/'

listholiday = '/api/v2/holidays/'

retrieveholiday = '/api/v2/holidays/'

updateholiday = '/api/v2/holidays/'

deleteholiday = '/api/v2/holidays/'

setovertimeratio = '/api/v2/overtime-ratio/'

getovertimeratio = '/api/v2/overtime-ratio/'

createshift = '/api/v2/shifts/'

deleteshift = '/api/v2/shifts/'

updateshift = '/api/v2/shifts/'

listshift = '/api/v2/shifts/'

retrieveshift = '/api/v2/shifts/'

listpunchtime = '/api/v2/punch-times/'

retrievepunchtime = '/api/v2/punch-times/'

listmonthlyreport = '/api/v2/attendance/monthly-reports/'

exportmonthlyreport = '/api/v2/attendance/monthly-reports/export/'

listdailyreport = '/api/v2/attendance/daily-reports/'

exportdailyreport = '/api/v2/attendance/daily-reports/export/'

listdj = '/api/v2/attendance/department-job-levels/'

updatedr = '/api/v2/attendance/daily-reports/'










