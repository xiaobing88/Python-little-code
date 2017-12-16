#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# student.xls 文件中的内容写到 student.xml 文件
import json
file = "student.txt"
with open(file, "r") as f:
    data = f.read()
data_n = json.loads(data)
print(data_n)
print(json.dumps(data_n))

import xml.dom.minidom

impl = xml.dom.minidom.getDOMImplementation()
dom = impl.createDocument(None, 'root', None)
root = dom.documentElement
citys = dom.createElement('citys')

root.appendChild(citys)
dd = str(json.dumps(data_n))
nameT=dom.createTextNode(dd)
citys.appendChild(nameT)
f= open('employees2.xml', 'w', encoding='utf-8')
dom.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
f.close()

