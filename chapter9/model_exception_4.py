#!/usr/bin/python3
# -*- coding:UTF-8 -*-

def model_exception(x,y):
    try:
        a = x/y
    except:
         print('Error happened')
    else:
        print('It went as expected')

model_exception(2,1)
