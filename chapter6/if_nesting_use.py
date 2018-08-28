#! /usr/bin/python3
# -*- coding:UTF-8 -*-

num = 10
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    elif num%4==0:
        print ("你输入的数字可以整除 2 和 4")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3 和 4")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")
