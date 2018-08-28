#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def default_param(name, age=23, addr='shanghai'):
    print(f'hi，我叫：{name}')
    print(f'我今年：{age}')
    print(f'我现在在: {addr}')
    return

print('-------传入必须参数-------')
default_param('小萌')
print('-------传入必须参数，更改第一个默认参数值-------')
default_param('小萌', 21)
print('-------传入必须参数，默认参数值都更改-------')
default_param('小萌', 21, 'beijing')
print('-------传入必须参数，指定默认参数名并更改参数值-------')
default_param('小萌', addr='beijing')
print('-------传入必须参数，指定参数名并更改值-------')
default_param('小萌', addr='beijing', age=23)
print('-------第一个默认参数不带参数名，第二个带-------')
default_param('小萌', 21, addr='beijing')
print('-------两个默认参数都带参数名-------')
default_param('小萌', age=23, addr='beijing')
print('-------第一个默认参数带参数名，第二个不带，报错-------')
# default_param('小萌',age=23,'beijing')  # 打开运行报错
