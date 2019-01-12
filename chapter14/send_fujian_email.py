#! /usr/bin/python
# -*-coding:UTF-8-*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = 'ai@test.com'
pwd = 'ai' #开通邮箱服务后，设置的客户端授权密码
receivers = ['lyz@163.com']  # 接收邮件，可设置为你的邮箱

#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("邮件测试", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

#邮件正文内容
message.attach(MIMEText('这是Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中就显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2)

try:
    # 使用非本地服务器，需要建立ssl连接
    smtpObj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
    smtpObj.login(sender, pwd)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as se:
    print(f"Error: 无法发送邮件.Case:{se}")
