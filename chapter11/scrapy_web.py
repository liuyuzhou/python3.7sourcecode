import re
import urllib.request
import urllib

from collections import deque
#使用队列存放url
queue = deque()
#使用visited防止重复爬同一页面
visited = set()

url = 'http://www.baidu.com'  # 入口页面, 可以换成别的
 #入队最初的页面
queue.append(url)
cnt = 0

while queue:
  url = queue.popleft()  # 队首元素出队
  visited |= {url}  # 标记为已访问

  print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
  cnt += 1

  try:
      #抓取页面
      urlop = urllib.request.urlopen(url,timeout=10)
  except Exception:
      print("超时")
      continue
  #判断是否为html页面
  if 'html' not in urlop.getheader('Content-Type'):
    continue

  # 避免程序异常中止, 用try..catch处理异常
  try:
   #转换为utf-8码
    data = urlop.read().decode('utf-8')
  except:
    continue

  # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
  linkre = re.compile("href=['\"]([^\"'>]*?)['\"].*?")
  for x in linkre.findall(data):##返回所有有匹配的列表
    if 'http' in x and x not in visited:##判断是否为http协议链接，并判断是否抓取过
      queue.append(x)
      print('加入队列 --->  ' + x)