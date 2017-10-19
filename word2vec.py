# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:46:44 2017

@author: zqx
"""
#引入word2vec
from gensim.models import word2vec  
#引入日志配置
import logging  
   
   
# 主程序  
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)  

# 加载语料  
sentences =word2vec.Text8Corpus(u"data2result.txt")  

#训练skip-gram模型，默认window=5  
'''
size参数主要是用来设置神经网络的层数，Word2Vec 中的默认值是设置为100层。
    是每个词的向量维度
 更大的层次设置意味着更多的输入数据，不过也能提升整体的准确度，合理的设置范围为 10~数百。
min_count:
    在不同大小的语料集中，我们对于基准词频的需求也是不一样的。譬如在较大的语料集中，
    我们希望忽略那些只出现过一两次的单词，这里我们就可以通过设置min_count参数进行控制。
    一般而言，合理的参数值会设置在0~100之间。
    min-count设置最低频率，默认是5，如果一个词语在文档中出现的次数小于5，那么就会丢弃
    
workers参数用于设置并发训练时候的线程数，不过仅当Cython安装的情况下才会起作用

window：是词向量训练时的上下文扫描窗口大小，窗口为5就是考虑前5个词和后5个词
'''
    
model =word2vec.Word2Vec(sentences, size=200)   
   
print model  
# 计算两个词的相似度/相关程度  
try:  
    y1 = model.similarity(u"信息", u"消息")  
except KeyError:  
    y1 = 0  
print u"【信息】和【消息】的相似度为：", y1  
print"-----\n"  
#  
# 计算某个词的相关词列表  
y2 = model.most_similar(u"资产", topn=20)  # 20个最相关的  
print u"和【资产】最相关的词有：\n"  
for item in y2:  
    print item[0], item[1]  
print"-----\n"  
   
# 寻找对应关系  
print u"炒股-借款，期限-"  
y3 =model.most_similar([u'借款', u'期限'], [u'炒股'], topn=3)  
for item in y3:  
    print item[0], item[1]  
print"----\n"  
   
# 寻找不合群的词  
y4 =model.doesnt_match(u"证券 基金 管理 国企".split())  
print u"不合群的词：", y4  
print"-----\n"  
   
# 保存模型，以便重用  
model.save(u"data2result.model")  
model.save(u"data2result.vector")  
# 对应的加载方式  
# model_2 =word2vec.Word2Vec.load("text8.model")  
   
# 以一种c语言可以解析的形式存储词向量  
#model.save_word2vec_format(u"书评.model.bin", binary=True)  
# 对应的加载方式  
# model_3 =word2vec.Word2Vec.load_word2vec_format("text8.model.bin",binary=True)  