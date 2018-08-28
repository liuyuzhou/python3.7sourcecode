#!/usr/bin/python3
# -*- coding:UTF-8 -*-

def use_finally(x,y):
    try:
        a = x/y
    except ZeroDivisionError:
        print('Some bad thing happened:division by zero')
    finally:
        print('No matter what happened,I will show in front of you')

use_finally(2,0)
