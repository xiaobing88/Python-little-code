#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import random, datetime
def create_code():
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    rand_num = random.randint(100, 1000)
    code = str(now_time) + str(rand_num)
    return code
code_list = [];i=0
while i < 200:
    code = create_code()
    code = "".join(sorted(code, reverse=True))
    if len(code) != 17:
        break
    if code not in code_list:
        code_list.append(code)
        i += 1
for j in code_list:print(j, end="\n")
