# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:00:04 2017

@author: zqx
"""

from gensim.models import word2vec
#####################导入模型#####################
model = word2vec.Word2Vec.load("data2result.model")

#####################模型评估#####################
'''
model.accuracy('data2result.model')
'''
#####################模型的使用#####################

#获取词向量
print model[u'金融']
type(model[u'金融'])
#输出的结果为：200维的数组,与参数size的设置相关

#计算一个词的最近似的词，倒排序
result = model.most_similar(u'金融')
for each in result:
    print each[0] , each[1]
    
#计算两词之间的余弦相似度
model.most_similar(positive=['603106', '1503'], negative=['45'])


sim1 = model.similarity(u'综合', u'贸易')
sim2 = model.similarity(u'阿里巴巴', u'有限公司')
sim3 = model.similarity(u'工程', u'广泛')

print sim1 
print sim2
print sim3

#计算两集合之间的余弦相似度(由于编码的问题，此处报错)
'''
list1 = [u'综合', u'贸易', u'阿里巴巴', u'广泛']
list2 = [u'报价',u'云计算', u'控股', u'经典']
list3 = [u'复兴', u'医药', u'金融', u'电气', u'中标']
list_sim1 =  model.n_similarity(list1, list2)
print list_sim1
list_sim2 = model.n_similarity(list1, list3)
print list_sim2
'''
#选出集合中不同类的词语
list = [u'综合', u'贸易', u'阿里巴巴', u'广泛']
print model.doesnt_match(list)
list = [u'复兴', u'医药', u'金融', u'电气', u'中标']
print model.doesnt_match(list)

##############Word2Vec 最著名的效果即是以语义化的方式推断出相似词汇########################
'''
model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
[('queen', 0.50882536)]
model.doesnt_match("breakfast cereal dinner lunch".split())
'cereal'
model.similarity('woman', 'man')
0.73723527
model.most_similar(['man'])
[(u'woman', 0.5686948895454407),
 (u'girl', 0.4957364797592163),
 (u'young', 0.4457539916038513),
 (u'luckiest', 0.4420626759529114),
 (u'serpent', 0.42716869711875916),
 (u'girls', 0.42680859565734863),
 (u'smokes', 0.4265017509460449),
 (u'creature', 0.4227582812309265),
 (u'robot', 0.417464017868042),
 (u'mortal', 0.41728296875953674)]
'''