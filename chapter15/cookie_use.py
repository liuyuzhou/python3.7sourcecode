import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar

url='http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=La2A2'
data={
    'username':'zhanghao',
    'password':'mima',
}
postdata=urllib.parse.urlencode(data).encode('utf8')
header={
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

request=urllib.request.Request(url,postdata,headers=header)
#使用http.cookiejar.CookieJar()创建CookieJar对象
cjar=http.cookiejar.CookieJar()
#使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
cookie=urllib.request.HTTPCookieProcessor(cjar)
opener=urllib.request.build_opener(cookie)
#将opener安装为全局
urllib.request.install_opener(opener)

try:
    reponse=urllib.request.urlopen(request)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)

fhandle=open('./test1.html','wb')
fhandle.write(reponse.read())
fhandle.close()

url2='http://bbs.chinaunix.net/forum-327-1.html'   #打开test2.html文件，会发现此时会保持我们的登录信息，为已登录状态。也就是说，对应的登录状态已经通过Cookie保存。
reponse2=urllib.request.urlopen(url)
fhandle2=open('./test2.html','wb')
fhandle2.write(reponse2.read())
fhandle2.close()