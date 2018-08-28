#!/usr/bin/python3
# -*- coding:UTF-8 -*-

class MyError(Exception):
    def __init__(self):
        pass

    def __str__(self):
       return 'this is self define error'

def my_error_test():
    try:
        raise MyError()
    except MyError as e:
        print('exception info:', e)

my_error_test()
