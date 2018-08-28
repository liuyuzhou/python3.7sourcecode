#! /usr/bin/python3
# -*-coding:UTF-8-*-

class DefaultInit(object):
    def __init__(self):
        print('我是不带参数的__init__方法。')

    def __init__(self, param):
        print(f'我是带一个参数的__init__方法，参数值为：{param}')

DefaultInit('hello')
print('类实例化结束。')

DefaultInit()
# DefaultInit('hello', 'world')
