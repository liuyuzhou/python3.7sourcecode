# -*- coding: utf_8 -*-
import urllib.request


# 伪装成浏览器(此处伪装成chrome)
HEADERS = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36')


# 取得网页内容
def get_content(url_path):
    opener = urllib.request.build_opener()
    # 将伪装成的浏览器添加到对应的http头部
    opener.addheaders=[HEADERS]
    # 读取相应的url
    read_contend = opener.open(url_path).read()
    # 将获得的html解码为utf-8
    data = read_contend.decode('utf-8')
    print(data)


if __name__ == "__main__":
    get_content('http://news.baidu.com/')