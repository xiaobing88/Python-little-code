#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）  内容写到 student.xls 文件中
import json,xlwt
file = "student.txt"
with open(file, "r") as f:
    data = f.read()
data_n = json.loads(data)
print(data_n)
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('student')
for i in data_n:
    worksheet.write(int(i)-1, 0, label=i)
    worksheet.write(int(i) - 1, 1, label=data_n[i][0])
    worksheet.write(int(i) - 1, 2, label=data_n[i][1])
    worksheet.write(int(i) - 1, 3, label=data_n[i][2])
    worksheet.write(int(i) - 1, 4, label=data_n[i][3])
workbook.save("student.xls")