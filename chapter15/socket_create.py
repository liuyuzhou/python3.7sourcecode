# 导入socket库
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname() 
# 设置端口号
port = 9999
# 连接服务，指定主机和端口
# s.connect((host, port))
s.connect(('www.baidu.com', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
