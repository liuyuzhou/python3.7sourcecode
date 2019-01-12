#! /usr/bin/python
# -*-coding:UTF-8-*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'ai@test.com'
pwd = 'ai' #开通邮箱服务后，设置的客户端授权密码
receivers = ['lyz@163.com']  # 接收邮件，可设置为你的邮箱

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header("邮件测试", 'utf-8')
message['To'] =  Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    # 使用非本地服务器，需要建立ssl连接
    smtpObj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
    smtpObj.login(sender, pwd)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as se:
    print(f"Error: 无法发送邮件.Case:{se}")
