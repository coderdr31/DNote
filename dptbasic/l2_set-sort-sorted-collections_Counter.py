#!/usr/bin/python3
# coding: utf-8

##################################################################
## set 集合
print(set([1,2,2,3])) # 返回种类，去掉重复值

##################################################################
## sort,sorted
# sort 覆盖原来, sorted 新建
xs = ['dddd','a','bb','ccc']
xs.sort(key=len)  # short to long

# len+reverse: long to short
xs.sort(key=len,reverse=True)
xs_new = sorted(xs,key=len,reverse=True)

##################################################################
## collections_Counter
# Counter
# Counter类的目的是用来跟踪值出现的次数。
from collections import Counter
a = [1, 2, 3, 1, 1, 2]
result = Counter(a)
print (result)
# 还可以返回出现最多的n个,排序
