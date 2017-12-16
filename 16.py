#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）  内容写到 student.xls 文件中
import json,xlwt
file = "numbers.txt"
with open(file, "r") as f:
    data = f.read()
data_n = json.loads(data)
print(data_n)
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('numbers')
for i in data_n:
    worksheet.write(data_n.index(i), 0, label=i[0])
    worksheet.write(data_n.index(i), 1, label=i[1])
    worksheet.write(data_n.index(i), 2, label=i[2])

workbook.save("numbers.xls")