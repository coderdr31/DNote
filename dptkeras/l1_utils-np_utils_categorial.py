#!/usr/bin/python3
# coding: utf-8

import numpy as np
from keras.utils import np_utils
##################################################################
## to_categorical(y, num_classes=None): 只能处理一维向量+数字, Converts a class vector (integers) to binary class matrix.
x = np.array([1, 2, 3]); print(x, x.shape)  # [1 2 3] (3,)
tmp_x = np_utils.to_categorical(x)
print(tmp_x.shape, tmp_x)  # (3, 4); 行代表 samples 个数, 列代表属性种类个数
# [[ 0.  1.  0.  0.]
#  [ 0.  0.  1.  0.]
#  [ 0.  0.  0.  1.]]
y = np.array([1, 3, 1])
print(np_utils.to_categorical(y))
# [[ 0.  1.  0.  0.]
#  [ 0.  0.  0.  1.]
#  [ 0.  1.  0.  0.]]
print(np_utils.to_categorical(y, num_classes=5))  # 还可以指定类别长度, 默认会自己计算
# [[ 0.  1.  0.  0.  0.]
#  [ 0.  0.  0.  1.  0.]
#  [ 0.  1.  0.  0.  0.]]
print(np_utils.to_categorical([0, 1]))
# [[ 1.  0.]
#  [ 0.  1.]]
# 发现会严格按照 integers 的位置来标注

## 与其他的区别
# sklearn.preprocessing.LabelEncoder() 不是onehot, 对不连续的数字或者文本-> 数字
# sklearn.preprocessing.oneHotEncoder() 多维(一维可转成多维), 数字-> onehot
# pandas.get_dummies() 只一维,文本/数字->one_hot

## 和 preprocessing.text.one_hot 对比
# keras.preprocessing.text.one_hot  # 是将文本处理成 index

## 和 sklearn.preprocessing.OneHotEncoder 区别见下面...
from sklearn import preprocessing
one_hot_encoder = preprocessing.OneHotEncoder()  # 输入要是多维,不能是一维
print(x.reshape(-1, 1))  # 3*1, -1占位符
print(one_hot_encoder.fit_transform(x.reshape(-1, 1)).toarray())  # 稀疏表示形式
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
print(one_hot_encoder.fit_transform(y.reshape(-1, 1)).toarray())  # 稀疏表示形式
# [[ 1.  0.]
#  [ 0.  1.]
#  [ 1.  0.]]
##################################################################
## normalize(x, axis=-1, order=2): Normalizes a Numpy array.
# 因为 scikit-learn 中实现的方法很多, 这里用到了在介绍
