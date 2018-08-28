import jieba

'''
cut方法有两个参数
1)第一个参数是我们想分词的字符串
2)第二个参数cut_all是用来控制是否采用全模式
'''

#全模式
word_list = jieba.cut("《Python 3.7 从零开始学》是一本得好好看看的好书！",cut_all=True)
print("全模式：","|".join(word_list))
#精确模式 , 默认就是精确模式
word_list = jieba.cut("《Python 3.7 从零开始学》是一本得好好看看的好书！",cut_all=False)
print("精确模式：","|".join(word_list))
#搜索引擎模式
word_list = jieba.cut_for_search("《Python 3.7 从零开始学》是一本得好好看看的好书！")
print("搜索引擎：","|".join(word_list))