#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 一个HTML文件，找出里面的正文
import requests
import re
url = "http://news.sicnu.edu.cn/page.php?act=view&contentId=17753&catId=22"

r = requests.get(url)
text = r.text

# result = re.findall(r"<.*?>(.*?)</.*?>", text)
# for i in result:print(i)

dr = re.compile(r'<[^>]+>',re.S)
dd = dr.sub('', text)
dd.replace("&nbsp;", "")
print(dd)