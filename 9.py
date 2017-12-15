#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 一个HTML文件，找出里面的链接。
import requests
import re
url = "http://news.sicnu.edu.cn/page.php?act=view&contentId=17753&catId=22"

r = requests.get(url)
text = r.text
# print(text)
result = re.findall(r"(http://.*?)[\"|<]", text)
for i in result:print(i)