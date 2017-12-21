#!/usr/bin/python3
# coding: utf-8

##################################################################
## 数据对齐和运算
# 自动对齐，行列的并集
df = pd.DataFrame(np.random.randn(10,4),columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['A', 'B', 'C'])
df + df2
df - df.iloc[0] # -行，默认行为是DataFrame的column和Series的index对齐，也就是对Series进行行广播
df.sub(df['A'], axis=0) #-key列
df * 5 + 2
# bool运算也行
# 转置，T属性(转置函数)
df.T

##################################################################
## DataFrame与NumPy函数的互用性
np.exp(df)
df.T.dot(df)  # dot方法能够实现DataFrame矩阵乘法
# s1.dot(s1) ,dot方法也能运用在Series上
