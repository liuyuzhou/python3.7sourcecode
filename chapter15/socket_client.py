#! /usr/bin/python3
# -*- coding:UTF-8 -*-

import socket

def socket_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取本地主机名
    host = socket.gethostname()
    port = 9999
    # 建立连接
    s.connect((host, port))
    # 接收欢迎消息
    print(s.recv(1024).decode('utf-8'))
    for data in ['小萌', '小智', '小强']:
       # 发送数据
       s.send(data.encode('utf-8'))
       print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

def main():
    socket_client()

if __name__ == '__main__':
    main()
