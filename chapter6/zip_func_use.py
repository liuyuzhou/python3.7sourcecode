#! /usr/bin/python3
#-*- coding:UTF-8 -*-

student=['xiaomeng','xiaozhi','xiaoqiang']
number=[1001,1002,1003]
for name,num in zip(student,number):
    print(f'{name}的学号是：{num}')
