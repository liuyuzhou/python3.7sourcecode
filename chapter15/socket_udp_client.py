#! /usr/bin/python3
# -*- coding:UTF-8 -*-

import socket

def socket_udp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in ['小萌', '小智']:
        host = socket.gethostname()
        port = 9999
        # 发送数据
        s.sendto(data.encode('utf-8'), (host, port))
        # 接收数据
        print(s.recv(1024).decode('utf-8'))
    s.close()

def main():
    socket_udp_client()

if __name__ == '__main__':
    main()
