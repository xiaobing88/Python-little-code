 #!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os

Father_Path = "C:/Risk2S/Python(test_document)/算法/"
# file_list = os.listdir(Father_Path)
# # print(file_list)
# for file in file_list:
#     file_path = Father_Path+file;print(file_path)
#     with open(file_path, 'rb') as f:
#         for i in f.readlines():
#             print(str(i, encoding='utf-8'))

filename = "0.py"
txt = open(filename, 'r')
lines = txt.readlines()

a = 0
b = 0
c = 0
for line in lines:
    if line[0] == '#':
        print(line)
        a += 1
    elif line=='\n':
        print(line)
        b += 1
    else:
        c += 1


print(a,b,c)