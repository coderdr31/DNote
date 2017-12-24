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

