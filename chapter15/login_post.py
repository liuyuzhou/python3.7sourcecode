#! /usr/bin/python3
# -*- coding:UTF-8 -*-

from urllib import request, parse

def login_post():
    print('Login to weibo.cn...')
    email = input('Email: ')
    passwd = input('Password: ')
    login_data = parse.urlencode([
        ('username', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer',
         'https://passport.weibo.cn/signin/welcome?'
         'entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])

    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent',
                   'Mozilla/6.0  AppleWebKit/536.26 '
                   '(KHTML, like Gecko) Version/8.0'
                   ' Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?'
                   'entry=mweibo&res=wel&wm=3349'
                   '&r=http%3A%2F%2Fm.weibo.cn%2F')

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print(f'Status:{f.status} {f.reason}')
        for k, v in f.getheaders():
            print(f'{k}: {v}')
            print(f"Data:{data.decode('utf-8')}")

def main():
    login_post()

if __name__ == "__main__":
    main()
