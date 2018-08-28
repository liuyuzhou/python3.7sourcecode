#!/usr/bin/python3
# -*- coding:UTF-8 -*-

def model_exception(x,y):
    try:
        a = x/y
        b = name
    except (ZeroDivisionError, NameError, TypeError) as e:
        print(e)

model_exception(2,'') 
