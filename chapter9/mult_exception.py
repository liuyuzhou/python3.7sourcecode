#!/usr/bin/python3
# -*- coding:UTF-8 -*-

def mult_exception(x,y):
    try:
        a = x/y
        b = name
    except ZeroDivisionError:
        print('this is ZeroDivisionError')
    except NameError:
        print('this is NameError')

mult_exception(2,0)
