1、运行 run.py 文件，可生成对应的几张图

或分别运行如下
info_search_360.py
info_search_baidu.py
info_search_sogou.py

三个文件，根据提示输入对应信息即可生成对应的几张图。

2、爬取到的结果信息在csvfile文件夹下

3、csv文件中有内容后，可以直接运行 wordcount_360.py,wordcount_baidu.py,wordcount_sogou.py  三个文件直接得到对应的图。


4、common文件夹中的 filter_words_360.py,filter_words_baidu.py,filter_words_sogou.py 三个文件中可以添加需要过滤或不需要
过滤的词组。

5、打开 wordcount_360.py,wordcount_baidu.py,wordcount_sogou.py 文件中的 “过滤不必要字符” 做不需要词组过滤；
打开 “需要字符” 筛选需要词组