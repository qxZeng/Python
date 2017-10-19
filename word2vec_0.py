# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:06:33 2017

@author: zqx
"""
########################模型的创建(训练生成模型)#############################
# 引入 word2vec
from gensim.models import word2vec

# 引入日志配置
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 引入数据集
raw_sentences = ["the quick brown fox jumps over the lazy dogs","yoyoyo you go home now to sleep"]

# 切分词汇
sentences= [s.encode('utf-8').split() for s in raw_sentences]
#print sentences

# 构建模型
model = word2vec.Word2Vec(sentences, min_count=1)

# 进行相关性比较
m = model.similarity('dogs','you')
print u"【dogs】和【you】的相似度为：", m

