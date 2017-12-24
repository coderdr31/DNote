#!/usr/bin/python3
# coding: utf-8
import numpy as np
import pandas as pd
##################################################################
## get_dummies 变量one-hot, 只能处理一维(包括Dataframe),文本/数字->0/1
# pandas.get_dummies(data, prefix=None, prefix_sep='_', dummy_na=False[忽略NAN])
s1 = ['a', 'b', np.nan]
print(pd.get_dummies(s1))
print(pd.get_dummies(s1,prefix="f",dummy_na=True))
