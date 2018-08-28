from urllib import request

class MovieTop(object):
    def __init__(self):
        self.start = 0
        self.param= '&filter='
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}

    def get_page(self):
        page_content = []
        try:
            while self.start <= 225:
                url = 'https://movie.douban.com/top250?start=' + str(self.start)
                req = request.Request(url, headers = self.headers)
                response = request.urlopen(req)
                page = response.read().decode('utf-8')
                page_num = (self.start + 25)//25
                print(f'正在抓取第{str(page_num)}页数据...' )
                self.start += 25
                page_content.append(page)
            return page_content
        except request.URLError as e:
            if hasattr(e, 'reason'):
                print(f'抓取失败，失败原因：{e.reason}')

    def main(self):
        print('开始从豆瓣电影抓取数据........')
        self.get_page()
        print('数据抓取完毕...')
