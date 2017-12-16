#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
import xlrd
data = xlrd.open_workbook("Risk2S2017_10.xls")
table = data.sheets()[0]#;print(table)
phone_time = table.col_values(3)[1:]#;print(phone_time)
class Conversion:
    def __init__(self, m, n):
        self.minute = m
        self.second = n
    def total(self):
        return (self.minute,self.second)

risk = []
for i in  phone_time:
    if "分" in i:
        minute = i.split("分")[0]
        second = i.split("分")[1][:-1]
        risk.append(Conversion(minute, second))
    else:
        minute = 0
        second = i[:-1]
        risk.append(Conversion(minute, second))
total_second = 0
total_minute = 0
for i in risk:
    total_minute += int(i.total()[0])
    total_second += int(i.total()[1])

print("本月总通话时间：{} 分 {} 秒".format(total_minute+(total_second//60), (total_second%60)))