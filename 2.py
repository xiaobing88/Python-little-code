#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import pymysql
code = """77644432222111110
87765444222111110
77766644222111110
98776442222111110
77644422211111100"""
data = code.split("\n")
# print(data)
db = pymysql.connect("localhost", "root", "root", "test")
cursor = db.cursor()
for i in data:
    insert_sql = """INSERT INTO `aaa_code` (`code`) VALUES ('{}')""".format(i)
    try:
        cursor.execute(insert_sql)
        db.commit()
    except:
        db.rollback()

sql = "select * from aaa_code"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
db.close()