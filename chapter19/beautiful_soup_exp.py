import requests
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'
# 创建实例
resp = requests.get(url)
# 创建对象
bs = BeautifulSoup(resp.content)
# 提取Tag
title_cont = bs.title
print(title_cont)
print(type(title_cont))
