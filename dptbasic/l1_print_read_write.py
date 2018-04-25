#!/usr/bin/python3
# coding: utf-8

##################################################################
## print()
a = 1
b = 'runoob'
print(a,b)
print("www","runoob","com",sep=".")  # 设置间隔符
print("the num of %s is %d" % (b, a)) # 格式化输出

##################################################################
## read()
##################################################################
# 格式
with open('/path/to/file', 'r') as f:
    f.xxxxxx

f = open('./l3_xlrd_xlwt.py', 'r')

for line in f:  # 最简单、最快速的逐行处理文本的方法：直接for循环文件对象
    print (line)

str = f.read()  # 一次性读取文件的全部内容放到一个字符串中(文件大于内存-不可行)

for line in f.readlines():  # 一次性读取文本的所有内容，结果是一个list
    print (line)  # 每行文本末尾都会带一个'\n'换行符 (可以使用L.rstrip('\n')去掉换行符）

# 读一行
line = f.readline()  # 速度慢
while line:
    print (line)
    line = f.readline()

f.close()


# 读取二维数组
list=[[item for item in line.strip().split()] for line in open('file').readlines()]

# 复杂版
# 文件内容：
# 包含w，h的行
# 含有空格的含有w 整数的h 行
# 4 3
# 1 2 3 4
# 2 3 4 5
# 6 7 8 9
with open('file') as f:
 w, h = [int(x) for x in f.readline().split()] # read first line
 array = []
 for line in f: # read rest of lines
 array.append([int(x) for x in line.split()])
#你可以将最后一个循环浓缩为嵌套列表理解
with open('file') as f:
 w, h = [int(x) for x in f.readline().split()]
 array = [[int(x) for x in line.split()] for line in f]

##################################################################
## write()
##################################################################
with open('/Users/michael/test.txt', 'w') as f:
    f.write('')

f1  = open('filename', 'w')
f1.write('内容')  # 输出后不换行
f1.close()

##################################################################
## 读写模式
r : 只读, 不创建, 不覆盖, 指针在开始
r+: 读写, 不创建, 不覆盖, 指针在开始
w : 只写, 会创建, 会覆盖, 指针在开始
w+: 读写, 会创建, 会覆盖, 指针在开始
a : 只写, 会创建, 不覆盖, 指针在结尾
a+: 读写, 会创建, 不覆盖, 指针在结尾
