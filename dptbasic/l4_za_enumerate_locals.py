#!/usr/bin/python3
# coding: utf-8

##################################################################
## enumerate() 同时列出数据和数据下标
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print i, element
##################################################################
## locals() 动态生成变量名
# locals() 返回当前作用域的所有变量,所以可以用这个函数来创建变量
for i in range(4):
    name='v'+str(i)
    locals()['v'+str(i)]=i

print v1,v2,v3
