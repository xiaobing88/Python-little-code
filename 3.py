#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import redis
code = """77644432222111110
87765444222111110
77766644222111110
98776442222111110
77644422211111100"""
data = code.split("\n")
# print(data)
r = redis.Redis(host="127.0.0.1", port=6379)
# r.lpush("aaa_code", " redis-2.10.6-py2.p")
for i in data:
    r.lpush("aaa_code", i)
for j in r.lrange("aaa_code", 0, 299):print(str(j, encoding='utf-8'))