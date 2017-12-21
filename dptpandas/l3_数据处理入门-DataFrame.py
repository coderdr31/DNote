#!/usr/bin/python3
# coding: utf-8
import pandas as pd
df = pd.read_csv('uk_rain_2014.csv', header=0) # 中文加encoding = 'gbk'，header数据列名-可省略
df.head(5) # 查看数据前几行
df.tail(5)
len(df) # 返回数据集的总行数-记录数

##################################################################
## 基本统计数据
pd.options.display.float_format = '{:,.3f}'.format # 将输出限制在3个小数位
df.describe() # 返回一张表，其中有诸如总数、均值、标准差之类的统计数据

##################################################################
## 过滤 (rain_octsep为列Key)
df.rain_octsep < 1000 # Or df['rain_octsep] < 1000 ，bool series
df[df.rain_octsep < 1000] # 这条代码只返回十月-九月降雨量小于 1000 mm 的记录
df[(df.rain_octsep < 1000) & (df.outflow_octsep < 4000)] # Can't use the keyword 'and'

## 字符串过滤
df[df.water_year.str.startswith('199')]

##################################################################
## 索引
df = df.set_index(['water_year']) # 将数据变为索引(一列设置为索引的时候，它就不再是数据的一部分了)
df = df.reset_index('water_year') # 将索引恢复为数据。
df.sort_index(ascending=False).head(5) # 按索引降序排列

##################################################################
##保存数据集
df.to_csv('uk_rain.csv')

##################################################################
## 网址[http://codingpy.com/article/a-quick-intro-to-pandas/]
## 对数据集应用函数
df['year'] = df.water_year.apply(base_year) # 对一列数据应用函数
applymap # 整个数据集

## 操作数据集的结构 groupby-分组
df.groupby(df.year // 10 *10).max()
decade_rain = df.groupby([df.year // 10 * 10, df.rain_octsep // 1000 * 1000])[['outflow_octsep',                                                              'outflow_decfeb', 'outflow_junaug']].mean()

## 合并数据集
uk_jpn_rain = df.merge(rain_jpn, on='year') # on 关键字来指定需要合并的列。通常你可以省略这个参数，Pandas 将会自动选择要合并的列。

## 使用 Pandas 快速作图
uk_jpn_rain.plot(x='year', y=['rain_octsep', 'jpn_rainfall'])
