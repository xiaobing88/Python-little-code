#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 任一个英文的纯文本文件，统计其中的单词出现的个数。
import jieba
from collections import Counter

# 词频统计
def word_count(word):
    v = Counter(word)
    k = 30
    print(('此文章最重要的'+str(k)+'个单词').center(25))
    # 最高出现次数的前n个
    # print(v.most_common(20))
    for i in v.most_common(k):
        print("词语: "+str(i[0]).ljust(5)+"\t\t次数： "+str(i[1]))

# 分词
def text_to_words(text):
    temp = jieba.cut(text, cut_all=True)
    word = []
    for i in temp:
        if i != None or '' or ' ':
            word.append(i)
    while '' in word:word.remove('')
    # print(word)
    return word

def main():
    try:
        # 读取文件中文本
        f = open('./english.txt', 'r')
        # print(f.read())
        text = f.read()
        word = text_to_words(text)
        word_count(word)
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()