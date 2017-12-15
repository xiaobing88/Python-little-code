#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
import os,re
from PIL import Image

pic_path = "C:/Risk2S/Python(test_document)/5_images/"
iphone5_width=1136
iphone5_depth=640
pics = os.listdir(pic_path)
# print(pics)
for pic in pics:
    path=pic_path+pic
    im = Image.open(path)
    w, h = im.size
    if w > iphone5_width:
        print("图片名称为"+pic+"图片被修改")
        h_new = int(iphone5_width*h/w)
        w_new = iphone5_width
        out = im.resize((w_new, h_new), Image.ANTIALIAS)
        new_pic = re.sub(pic[:-4], pic[:-4] + '_new', pic)
        # print(new_pic)
        new_path = path+new_pic
        out.save(new_path)
    if h > iphone5_depth:
        print("图片名称为"+pic+"图片被修改")
        w_new = int(iphone5_depth*w/h)
        h_new = iphone5_depth
        out = im.resize((w_new, h_new), Image.ANTIALIAS)
        new_pic = re.sub(pic[:-4], pic[:-4] + '_new', pic)
        # print(new_pic)
        new_path = path+new_pic
        out.save(new_path)
