#!/usr/bin/python3
# coding: utf-8
import numpy as np
import pandas as pd
##################################################################
## concat 简单轴融合
# pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,keys=None, levels=None, names=None, verify_integrity=False)
# axis： 需要合并链接的轴，0是行(纵向拼接)，1是列(行对齐,横向拼接)
# join：连接的方式 inner(交集)，或者outer(outer)
# join_axes: 根据那个轴来对齐数据 pd.concat([df1, df4], axis=1, join_axes=[df1.index])
# ignore_index: 置True无视index
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
print(pd.concat([s1, s2]))
print(pd.concat([s1, s2], ignore_index=True, keys=['s1', 's2'],names=['Series name', 'Row ID'])) # 忽视原先的index,给原先的打标记key
df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
print(pd.concat([df1, df2]))

##################################################################
## append 是series和dataframe的方法,默认纵向拼接(axis=0)
print(df1.append(df2))
