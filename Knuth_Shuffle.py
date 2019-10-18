# -*- coding:utf-8 -*-
#

import random

l = ['meicook','kfc','noodle','meicook','meicook']
f = []
i = 0
n = len(l)-1
for i in range(n+1):
	m = l[random.randint(0,n)]
	f.append(m)
	l.remove(m)
	n = n-1
print f

