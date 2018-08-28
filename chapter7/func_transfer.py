#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def no_return():
    print('no return函数不写return语句')

def just_return():
    print('just return函数只写return，不返回具体内容')
    return

def return_val():
    x=10
    y=20
    z=x+y
    print('return val函数写return语句，并返回求和的结果。')
    return z

print(f'函数no return调用结果：{no_return()}')
print(f'函数just return调用结果：{just_return()}')
print(f'函数return val调用结果：{return_val()}')
