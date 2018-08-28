#! /usr/bin/python3
# -*- coding:UTF-8 -*-

num = 100
def func_global():
    num = 200
    print(f'函数体中num的值为:{num}')

func_global()
print(f'函数外num的值为:{num}',)
