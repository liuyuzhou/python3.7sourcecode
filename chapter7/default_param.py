#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def default_param(name, age=23):
    print(f'hi，我叫：{name}')
    print(f'我今年：{age}')
    return

default_param('小萌')
default_param('小萌',21)
