#!/usr/bin/python3
# coding: utf-8
import numpy as np
import pandas as pd

##################################################################
## 带有标签的列和索引,从csv导入数据，对数据过滤和转换

##################################################################
## series 一维带label(index)的数组，元素可以是任何数据类型(数，字符，python对象),元素的数据类型可不同。series值可变，大小不可变
# s = pd.Series(data, index=index) ,data(Python字典,ndarray,标量数值) index是label列表
## data为ndarray,index和data的长度一定要一样
print(pd.Series(np.random.randn(5)))  # 若没有指明index,默认数字index
s = pd.Series([0,1,2,3,4], index=['a', 'b', 'c', 'd', 'e'])
print(s.index)

## data为dict,index和data的长度可不同，也可不提供index。此时，lable以dictKey为准
d = {'a' : 0., 'b' : 1., 'c' : 2.}
print(pd.Series(d))
print(pd.Series(d, index=['b', 'c', 'd', 'a'])) # d为NAN

## data为标量值，一定要有index。为了匹配index的长度，该数值将被重复
print(pd.Series(5., index=['a', 'b', 'c', 'd', 'e']))
# series可看成ndarry
print(s[0]) # value
print(s[:3],s[[4,3,1]]) # key-value
print(np.exp(s))
# series可看成dict
print(s['a']) # value
s['e'] = 12.
print('e' in s)
print(s.get('e'))

## Series和ndarray之间的主要区别是，Series之间的操作会基于label对数据自动对齐
print(s[1:] + s[:-1]) # lable不一样，结果为并集，有值的为交集
print(s)
print(s[1:])
print(s[:-1])

##################################################################
## DataFrame 带label的二维数据结构，index(行lable),columns(key 列lable)
# 输入：字典(普通字典，或一维ndarray字典、列表字典、Series字典), 二维ndarray, series, DataFrame, 支持传入index(行label)和columns(列label)参数
## series字典，结果的index是各个Series的index的并,columns默认为字典Key
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
      'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])} # series字典
df = pd.DataFrame(d)
print(df)
# 行label和列label可分别通过访问index和columns获取
df.index.name = "char"  # 给列的index赋值
print(df.index, df.columns)
print(pd.DataFrame(d, index=['d','b','a'])) # 指定index
print(pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])) # 指定列

## ndarray字典 列表字典
# ndarrays必须具有相同的长度。如果传入index参数，它的长度也必须和ndarray长度相同。
d = {'one' : [1., 2., 3., 4.],
      'two' : [4., 3., 2., 1.]}
pd.DataFrame(d)
pd.DataFrame(d, index=['a', 'b', 'c', 'd'])

## 字典列表
data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
print(pd.DataFrame(data2))
print(pd.DataFrame(data2, columns=['a','b']))
print(pd.DataFrame(data2, index=['first','second']))

## 列选择，添加，删除
# 可以把DataFrame看做Series构成的字典，使用和字典同样的操作来增加列、删除列、对列重新赋值
print(df['one']) # 同 df.one
df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
# 列可以删除或像字典一样被弹出
del df['two']
three = df.pop('three')
# 列插入
df['foo'] = 'bar' # 当插入一个标量值，它自然会被填充到列中
df['one_trunc'] = df['one'][:2] # 默认插到最后一列，符合index索引顺序
df.insert(1,'bar',df['one']) # insert(列号，列名key，data)
# 用方法链来分配新列,DataFrame有一个assign()方法，利用现有列来创建新列。

## 检索
# 操作	              语法	         结果
# 列选择	          df[col]	    Series
# 通过label来选择行	  df.loc[label]	Series
# 通过下标选择行	  df.iloc[loc]	Series
# 选择部分行	      df[5:10]	    DataFrame
# 通过布尔向量选择行  df[bool_vec]	DataFrame
print(df)
print(df.loc['b']) # 同df.iloc[1]
