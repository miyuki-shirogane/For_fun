#-*-coding:utf-8-*-

# a = [1,2,3]
# b = [4,5]
# c=a.extend(b)
# print a
# print b
# print c


 
# Fibonacci Sequence递归解决斐波那契数列前20项的输出
# lis =[]
# for i in range(20):
#     if i ==0 or i ==1:
#         lis.append(1)
#     else:
#         lis.append(lis[i-2]+lis[i-1])
# print(lis)



list = [1,2,3,4,5]
list_s = []
for j in list:
    if j >= 1 and j <= 5:
        list_s.append(1)
    else:
        list_s.append(0)
s=1
for i in list_s:
    s*=i
if s == 1:
	print 'true'
else:
	print 'false'


