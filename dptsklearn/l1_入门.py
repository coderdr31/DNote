#!/usr/bin/python3
# coding: utf-8

##################################################################
## 简例
from sklearn import datasets
# 加载数据集
iris = datasets.load_iris() # 载入数据集
digits = datasets.load_digits()
print(digits.data) # 数据存储在.data中
print(digits.target) # 类别变量存储在.target成员中
print(digits.images[0])

# 模型
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1]) # 数据(训练集除了最后一个)学习
print(clf.predict(digits.data[-1:])) # 预测最后一张图片
# 用matplot画图
print(__doc__)
import matplotlib.pyplot as plt
# 画最后一个数据
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
