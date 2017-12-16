#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 纯文本文件 city.txt为城市信息, 里面的内容  内容写到 city.xls
import json,xlwt
file = "city.txt"
with open(file, "r") as f:
    data = f.read()
data_n = json.loads(data)
print(data_n)
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('city')
for i in data_n:
    worksheet.write(int(i)-1, 0, label=i)
    worksheet.write(int(i) - 1, 1, label=data_n[i])
workbook.save("city.xls")