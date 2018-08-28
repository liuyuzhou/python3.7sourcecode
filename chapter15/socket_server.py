#! /usr/bin/python3
# -*- coding:UTF-8 -*-

import socket
import threading
import time

def socket_server():
    # 创建 socket 对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取本地主机名
    host = socket.gethostname()

    port = 9999

    # 绑定端口
    server_socket.bind((host, port))

    # 设置最大连接数，超过后排队
    server_socket.listen(5)

    while True:
        # 接受一个新连接
        sock, addr = server_socket.accept()
        # 创建新线程处理TCP连接
        t = threading.Thread(target=tcp_link, args=(sock, addr))
        t.start()

def tcp_link(sock, addr):
    print(f'Accept new connection from {addr}...')
    sock.send('欢迎学习Python网络编程!'.encode('utf-8'))
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print(f'Connection from {addr} closed.')

def main():
    socket_server()

if __name__ == '__main__':
    main()
