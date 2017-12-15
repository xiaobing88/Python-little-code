#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
import re
with open("./filtered_words.txt", 'r') as f:
    words = f.readlines()
    # 列表推导式
    word_list = [i.replace('\n', '') for i in words]
print("敏感词：")
for w in word_list:print(w, end='\t')
print("\n")
while True:
    user_input = input("用户输入：")
    for i in word_list:
        result = re.findall(r"{}".format(i), user_input)
        if len(result) == 1:
            user_input = user_input.replace(result[0], str(len(result[0]) * "*"))
    print(user_input)