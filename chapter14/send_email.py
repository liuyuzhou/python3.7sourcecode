#! /usr/bin/python
# -*-coding:UTF-8-*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'ai@test.com'
pwd = 'ai' #开通邮箱服务后，设置的客户端授权密码
receivers = ['lyz@163.com']  # 接收邮件，可设置为你的邮箱   # 接收邮件，可设置为你的邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("邮件测试", 'utf-8')
message['To'] =  Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    # 使用非本地服务器，需要建立ssl连接
    smtpObj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
    # smtplib.SMTP
    smtpObj.login(sender, pwd)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as se:
    print(f"Error: 无法发送邮件.Case:{se}")
