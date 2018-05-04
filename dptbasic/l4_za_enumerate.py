#!/usr/bin/python3
# coding: utf-8

##################################################################
## enumerate() 同时列出数据和数据下标
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print i, element
