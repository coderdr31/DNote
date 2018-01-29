#!/usr/bin/python
# coding=utf-8
import xlrd

###########################
# sudo pip install xlrd
# 直接执行；fname=要读取的xlsx名字；可找出多个sheet，所有的值  #
###########################

fname = "./in_file/ReadXlsx_Book1.xlsx"
bk = xlrd.open_workbook(fname)
for k in range(bk.nsheets):
    sheet_name = "Sheet" + str(k + 1)
    try:
        sh = bk.sheet_by_name(sheet_name)
    except:
        print "no sheet in %s named Sheet1" % fname
        # return None
    else:
        print sheet_name
    nrows = sh.nrows
    ncols = sh.ncols
    print "nrows %d, ncols %d" % (nrows, ncols)

    cell_value = sh.cell_value(0, 0)  # 读单个的值
    # print cell_value

    row_list = [[] for i in range(nrows)]
    for i in range(0, nrows):
        # print sh.row_values(i) #读出一行的值，是列表形式
        for j in range(0, ncols):
            row_list[i].append(sh.cell_value(i, j))
            # 或者 row_list[i].append(sh.row_values(i)[j])
        print row_list[i]

##################################################################
## 针对 03版excel（xls结尾的），我们可以使用xlrd读，xlwt包来写
## http://qindongliang.iteye.com/blog/2163700
import xlwt
path = "1.xls"
wb=xlwt.Workbook()
sheet=wb.add_sheet("xlwt数据测试表")
value = [["名称", "hadoop编程实战", "hbase编程实战", "lucene编程实战"], ["价格", "52.3", "45", "36"], ["出版社", "机械工业出版社", "人民邮电出版社", "华夏人民出版社"], ["中文版式", "中", "英", "英"]]
for i in range(0,4):
    for j in range(0,len(value[i])):
        sheet.write(i,j,value[i][j])
wb.save(path)
print("写入数据成功！")
