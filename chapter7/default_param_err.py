#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def default_param_err(age=23, name):
	print(f'hi，我叫：{name}')
	print(f'我今年：{age}')
	return

default_param_err(age=21,name='小萌')
