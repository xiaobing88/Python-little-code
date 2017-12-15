#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

with open("./filtered_words.txt", 'r') as f:
    words = f.readlines()
    # 列表推导式
    word_list = [i.replace('\n', '') for i in words]
print("敏感词：")
for w in word_list:print(w, end='\t')
print("\n")
while True:
    user_input = input("用户输入：")
    if user_input in word_list:
        print("程序输出：Freedom")
    else:
        print("程序输出：Human Rights")