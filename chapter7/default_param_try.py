#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def default_param_1(age=23, name, addr='shanghai'):
	print(f'hi，我叫：{name}')
	print(f'我今年：{age}')
	print(f'我现在在: {addr}')
	return

def default_param_2(age=23, addr='shanghai', name):
	print(f'hi，我叫：{name}')
	print(f'我今年：{age}')
	print(f'我现在在: {addr}')
	return

default_param_1(age=23, '小萌',addr='shanghai')
default_param_2(age=23, addr='shanghai', '小萌')
