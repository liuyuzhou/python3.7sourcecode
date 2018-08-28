#!/usr/bin/python3
# -*- coding:UTF-8 -*-


def exp_exception(x,y):
    try:
        a = x/y
        print('a=', a)
        return a
    except Exception:
        print('程序出现异常，异常信息：被除数为0')

exp_exception(2, 0)
