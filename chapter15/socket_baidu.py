#! /usr/bin/python3
# -*- coding:UTF-8 -*-

import socket

def socket_client():
    # 创建 socket 对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取主机名
    host = 'www.baidu.com'
    # 设置端口号
    port = 80
    # 连接服务，指定主机和端口
    s.connect((host, port))
    #发送数据
    s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
    # 接收数据
    buffer = []
    while True:
        # 每次最多接收1k字节
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)

    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件
    with open('baidu.html', 'wb') as f:
        f.write(html)
    s.close()

def main():
    socket_client()

if __name__ == '__main__':
    main()
