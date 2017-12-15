#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

# 原始文本
text = "线程是程序执行时的最小单位，它是进程的一个执行流，\
        是CPU调度和分派的基本单位，一个进程可以由很多个线程组成，\
        线程间共享进程的所有资源，每个线程有自己的堆栈和局部变量。\
        线程由CPU独立调度执行，在多CPU环境下就允许多个线程同时运行。\
        同样多线程也可以实现并发操作，每个请求分配一个线程来处理。"

def TF_IDF(text):
    from jieba import analyse
    # 引入TF-IDF关键词抽取接口
    tfidf = analyse.extract_tags
    # 基于TF-IDF算法进行关键词抽取
    keywords = tfidf(text)
    for i in keywords:
        print(i, end='\t')

def TextRank(text):
    from jieba import analyse
    # 引入TextRank关键词抽取接口
    textrank = analyse.textrank
    keywords = textrank(text)
    for i in keywords:
        print(i, end='\t')

# TF_IDF(text)
TextRank(text)