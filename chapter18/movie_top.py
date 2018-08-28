#! /usr/bin/python3
# -*- coding:UTF-8 -*-

from urllib import request
import re

class MovieTop(object):
      def __init__(self):
         self.start = 0
         self.param= '&filter='
         self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
         self.movie_list = []
         self.file_path = 'D:\movie_spider.txt'

      def get_page(self):
          try:
             url = 'https://movie.douban.com/top250?start=' + str(self.start)
             req = request.Request(url, headers = self.headers)
             response = request.urlopen(req)
             page = response.read().decode('utf-8')
             page_num = (self.start + 25)//25
             print(f'正在抓取第{str(page_num)}页数据...' )
             self.start += 25
             return page
          except request.URLError as e:
             if hasattr(e, 'reason'):
                 print(f'抓取失败，失败原因：{e.reason}')

      def get_movie_info(self):
          pattern = re.compile(u'<div.*?class="item">.*?'
                              + u'<div.*?class="pic">.*?'
                              + u'<em.*?class="">(.*?)</em>.*?'
                              + u'<div.*?class="info">.*?'
                              + u'<span.*?class="title">(.*?)'
                              + u'</span>.*?<span.*?class="title">(.*?)</span>.*?'
                              + u'<span.*?class="other">(.*?)</span>.*?</a>.*?'
                              + u'<div.*?class="bd">.*?<p.*?class="">.*?'
                              + u'导演: (.*?)&nbsp;&nbsp;&nbsp;.*?<br>'
                              + u'(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;'
                              + u'(.*?)</p>.*?<div.*?class="star">.*?'
                              + u'<span.*?'
                              + u'class="rating_num".*?property="v:average">'
                              + u'(.*?)</span>.*?'
                              + u'.*?<span>(.*?)人评价</span>.*?'
                              + u'<p.*?class="quote">.*?'
                              + u'<span.*?class="inq">(.*?)'
                              + u'</span>.*?</p>', re.S)

          while self.start <= 225:
              page = self.get_page()
              movies = re.findall(pattern, page)
              for movie in movies:
                  self.movie_list.append([movie[0], movie[1],
                                          movie[2].lstrip('&nbsp;/&nbsp;'),
                                          movie[3].lstrip('&nbsp;/&nbsp;'),
                                          movie[4],
                                          movie[5].lstrip(),
                                          movie[6],
                                          movie[7].rstrip(),
                                          movie[8],
                                          movie[9],
                                          movie[10]])

      def write_text(self):
          print('开始向文件写入数据.........')
          file_top = open(self.file_path, 'w', encoding='utf-8')
          try:
              for movie in self.movie_list:
                file_top.write('电影排名：' + movie[0] + '\r\n')
                file_top.write('电影名称：' + movie[1] + '\r\n')
                file_top.write('外文名称：' + movie[2] + '\r\n')
                file_top.write('电影别名：' + movie[3] + '\r\n')
                file_top.write('导演姓名：' + movie[4] + '\r\n')
                file_top.write('上映年份：' + movie[5] + '\r\n')
                file_top.write('制作国家/地区：' + movie[6] + '\r\n')
                file_top.write('电影类别：' + movie[7] + '\r\n')
                file_top.write('电影评分：' + movie[8] + '\r\n')
                file_top.write('参评人数：' + movie[9] + '\r\n')
                file_top.write('简短影评：' + movie[10] + '\r\n\r\n')
              print('抓取结果写入文件成功...')
          except Exception as e:
              print(e)
          finally:
              file_top.close()


      def main(self):
         print('开始从豆瓣电影抓取数据........')
         self.get_movie_info()
         self.write_text()
         print('数据抓取完毕...')

dou_ban_spider = MovieTop()
dou_ban_spider.main()
