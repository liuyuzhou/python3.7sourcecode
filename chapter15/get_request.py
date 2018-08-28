#! /usr/bin/python3
# -*- coding:UTF-8 -*-

from urllib import request

def get_request():
    with request.urlopen('http://www.baidu.com') as f:
        data = f.read()
        print(f'Status:{f.status} {f.reason}')
        for k, v in f.getheaders():
            print(f'{k}: {v}')
    print(f"Data:{data.decode('utf-8')}")

def main():
    get_request()

if __name__ == "__main__":
    main()
