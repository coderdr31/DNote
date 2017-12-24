#!/usr/bin/python3
# coding: utf-8
from sklearn import preprocessing

##################################################################
## LabelEncoder是对不连续的数字或者文本-> 数字
le = preprocessing.LabelEncoder()
print(le.fit([1, 2, 2, 6])) # 导入数据 >LabelEncoder()
print(le.classes_) # 输出类别，[1 2 6]
print(le.transform([1, 1, 2, 6])) # 转换 [0 0 1 2]
# fit_transform(y) 作用为fit+transform
print(le.inverse_transform([0, 0, 1, 2])) # 反向转换 [1 1 2 6]
## 非数值-> 数字
le = preprocessing.LabelEncoder()
le.fit(["paris", "paris", "tokyo", "amsterdam"])
print(le.classes_) # ['amsterdam' 'paris' 'tokyo']
print(list(le.classes_)) # ['amsterdam', 'paris', 'tokyo']
print(le.transform(["tokyo", "tokyo", "paris"])) # [2 2 1]
print(list(le.inverse_transform([2, 2, 1])))

##################################################################
## OneHotEncoder 多维. np.array([0, 1, 2]).reshape(-1, 1)可变为多维
# 无法直接处理字符串值. 文本要先转换为数字,再用 oneHotEncoder
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
print(enc.n_values_)  # array of shape (n_features,), 特征的大小位数
print(enc.feature_indices_)  # 第几个到第几个表示某特征
print(enc.transform([[0, 1, 1]]).toarray())
# [[ 1.  0.  0.  1.  0.  0.  0.  0.  1.]]
# fit 了 4 个数据 3 个特征, 而 transform 了 1 个数据 3 个特征. 第一个特征两种值(0: 10, 1: 01), 第二个特征三种值(0: 100, 1: 010, 2: 001),
# 第三个特征四种值(0: 1000, 1: 0100, 2: 0010, 3: 0001). 所以转换[0, 1, 3]为[ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  1.].

# keras.utils.np_utils.to_categorical(x) one-hot一维的

