# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:34:50 2017

@author: zqx
"""
import jieba

with open('F:\\python2.7\data.txt','r') as f:
    for line in f:
        seg = jieba.cut(line.strip(), cut_all = False)
        s= ' '.join(seg)
        m=list(s)
        with open('data2result.txt','a+')as f:
            for word in m:
                f.write(word.encode('utf-8'))
                #print word
