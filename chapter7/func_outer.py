#! /usr/bin/python3
# -*- coding:UTF-8 -*-

x = 50
def func_outer(x):
    print(f'x等于:{x}')
    x = 2
    print(f'局部变量x变为:{x}')
func_outer(x)
print(f'x一直是:{x}')
