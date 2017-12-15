#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)http://tieba.baidu.com/p/2166231880
import requests,re

url = "http://tieba.baidu.com/p/2166231880"
r = requests.get(url)
html = r.text
imgs_url = re.findall(r"http://imgsrc.baidu.com/forum/.*?.jpg", html)
x = 0
for image in imgs_url:
    ir = requests.get(image, stream=True)
    if ir.status_code == 200:
        x += 1
        with open('./12_images/logo{}.jpg'.format(x), 'wb') as f:
            for chunk in ir:
                f.write(chunk)