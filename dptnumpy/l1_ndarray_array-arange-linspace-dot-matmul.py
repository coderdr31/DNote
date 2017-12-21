#!/usr/bin/python3
# coding: utf-8
# numpy是个数学库,数组计算，向量、矩阵
import numpy as np

##################################################################
## 多维数组ndarray 一多维数组，向量 矩阵,dtype数据类型
## 创建数组
a = np.array([0, 1, 2, 3, 4])
b = np.array((0, 1, 2, 3, 4))
c = np.arange(5)
d = np.linspace(0, 4, 5)
print(a, b, c, d) # >>>[0 1 2 3 4] [0 1 2 3 4] [0 1 2 3 4] [ 0.  1.  2.  3.  4.]
print(a[3]) # >>>3 索引
print(a[1:3]) # >>>[1 2] 切片
## numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None) 在指定的间隔内返回均匀间隔的数字,endpoint默认为true 输出包括stop,但retstep为true还会返回step
print(np.linspace(1, 10, 10)) # [  1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]
print(np.linspace(1, 10, 10, endpoint = False)) # [ 1.   1.9  2.8  3.7  4.6  5.5  6.4  7.3  8.2  9.1]
print(np.linspace(1, 10, 10, endpoint = False, retstep= True)) # (array([ 1. ,  1.9,  2.8,  3.7,  4.6,  5.5,  6.4,  7.3,  8.2,  9.1]), 0.90000000000000002)
print(type(a))
## np.arange & 索引
a = np.arange(0, 100, 10)
indices = [1, 5, -1]
b = a[indices]
c = a[a >= 50]
print(a) # >>>[ 0 10 20 30 40 50 60 70 80 90]
print(b) # >>>[10 50 90]
print(c) # >>>[50 60 70 80 90]

##################################################################
## nD Array,切片，多个数组指向同一地址空间
x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(type(x))  # >>> <type 'numpy.ndarray'>
print(x.shape, x.ndim, x.size) # >>> (2, 3) 数组维数2 元素数6
print(x.dtype)  # >>> int32
y = x[:,1] # 指向同一地址空间
print(y) # >>> [2 5] 第三列
y[0] = 9 # y>>> [9 5]
print(x) # >>> [[1 9 3] [4 5 6]]
print(x.item)
## 复杂多维数组切片,索引
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

print(a[2,4]) # >>>25
print(a[0, 1:4]) # >>>[12 13 14]
print(a[1:4, 0]) # >>>[16 21 26]
print(a[::2,::2]) # >>>[[11 13 15]
                  #     [21 23 25]
                  #     [31 33 35]]
print(a[:, 1]) # >>>[12 17 22 27 32]

##################################################################
## where 函数
a = np.arange(0, 100, 10)
b = np.where(a < 50)
c = np.where(a >= 50)[0]
print(b) # >>>(array([0, 1, 2, 3, 4]),) 相当与给出下标
print(a[b]) # >>>[ 0 10 20 30 40]
print(c) # >>>[5 6 7 8 9]

##################################################################
## 计算 定轴操作axis
print(x.sum(axis=0),x.sum(1)) # >>> [ 5 14  9] [13 15] 在轴上求和
# 类似还有 min,max,cumsum

##################################################################
## Arithmetic, matrix multiplication, and comparison operations
## Basic Operators
a = np.arange(25) # >>> [0-24]一维数组
a = a.reshape((5, 5)) # >>> 5*5数组

b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
              4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
              56, 3, 56, 44, 78])
b = b.reshape((5,5))
## 数组逐元素运算返回数组。比如 (a, b, c) + (d, e, f) >>> (a+d, b+e, c+f)。
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2) # 指数，平方
print(a < b)
print(a > b)
## dot()计算两个数组的点积,返回标量。
# 矩阵乘法
print(a.dot(b))
print(a.__matmul__(b)) # 矩阵乘法，和dot()效果一样
# 还有很多__xxxx__的方法
