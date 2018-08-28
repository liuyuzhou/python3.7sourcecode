#! /usr/bin/python3
# -*- coding:UTF-8 -*-

num = 100
print(f'函数调用前num的值为:{num}')
def func_glo_1():
    global num
    num = 200
    print(f'函数体中num的值为:{num}')

func_glo_1()
print(f'函数调用结束后num的值为:{num}')
