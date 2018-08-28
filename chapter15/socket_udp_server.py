#! /usr/bin/python3
# -*- coding:UTF-8 -*-

import socket

def socket_udp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostname()
    port = 9999
    # 绑定端口
    s.bind((host, port))

    while True:
        # 接收数据
        data, addr = s.recvfrom(1024)
        print(f'Received from {addr}.')
        s.sendto(b'hello, %s,welcome!' % data, addr)

def main():
    socket_udp_server()

if __name__ == "__main__":
    main()
