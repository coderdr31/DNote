#!/bin/bash
##################################################################
## head
head -n -1000  # 最后1000行过滤掉
head -n 1000  # 显示前面1000行

##################################################################
## tail
tail -n 1000  # 显示最后1000行
tail -n +1000  # 从1000行开始显示，显示1000行以后的
cat filename| head -n 3000 | tail -n +1000  #  显示1000行到3000行
cat filename | tail -n +3000 | head -n 1000  # 从第3000行开始，显示1000行。即显示3000~3999行

##################################################################
## sed
sed -n '5,10p' filename  # 查看文件的第5行到第10行。
## sed 还有编辑文件的功能
sed 's/^/xxx/' filename > output  # 每行行首添加字符串(^符号代表行首)
sed 's/$/xxx/' filename > output  # 每行行尾添加字符串($符号代表行尾)
sed -i '1i xxxx' filename # 在第一行插入一行(-i 改变了filename)
sed '1i xxxx' filename > output # 在第一行插入一行(没改变filename)
# 删除
sed -i '1d' filename  # 删除首行
