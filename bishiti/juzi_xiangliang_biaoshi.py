# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:19:19 2016

@author: Jhy1993
向量表示
题目描述
小B所在的团队正在开发一个WEB输入内容相似性检测应用，她想到的一种方法是统计用户输入内容中不同单词的出现频率，据此建立一个向量表示用户输入的内容。
用户输入的内容已经经过过滤处理，只剩下单词和空格，没有标点符号。
各个单词出现频率按从小到大的顺序排列后，即构成了用户输入内容的向量表示。
由于用户输入的内容可能很长，单靠人力完全无法找出来。因此小B希望你能帮忙编写一个程序，输出用户内容的向量表达。

输入
输入包括若干行文本数据，每行表示一个用户输入文档。一行文本由单词和空格组成，单词之间由空格分隔，最多不超过10000个ASCII码字符。

样例输入
a bd a d
b abc b a a
输出
对于每个用户输入文档，输出一行向量表示，数值之间用空格分隔。
样例输出
1 1 2
1 2 2
"""
while 1:
    s = raw_input()
    s = list(s.split())
    s_u = list(set(s))
    num = list()
    for i in s_u:
        n = s.count(i)
        num.append(n)
    nn = sorted(num)
    for i in range(len(nn)):
        print nn[i],
    
    






















