#! /usr/bin/python3
# -*- coding:UTF-8 -*-
# import sys
#
# sys.setrecursionlimit(10000) #例如这里设置深度为一万

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(f'调用递归函数执行结果为：{fact(997)}')