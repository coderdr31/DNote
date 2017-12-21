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
## OneHotEncoder
