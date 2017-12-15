#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
from PIL import Image, ImageDraw, ImageFont

def qq_num():
    num = str(4)
    img = Image.open('./qq.png')
    h, l = img.size

    font = ImageFont.truetype('./arial.ttf', 40)
    draw = ImageDraw.Draw(img)

    draw.text((h * 0.8, l * 0.05), num, (255, 33, 33), font=font)
    img.show()
    # img.save('./qq2.png', 'png')

qq_num()
