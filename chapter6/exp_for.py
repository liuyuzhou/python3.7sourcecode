#! /usr/bin/python3
# -*- coding:UTF-8 -*-

print('-----for循环字符串-----------')
for letter in 'good':    #for循环字符串
   print (f'当前字母 :{letter}')

print('-----for循环数字序列-----------')
number=[1,2,3]
for num in  number:    #for循环数字序列
    print(f'当前数字：{num}')

print('-----for循环字典-----------')
tups={'name':'小智','number':'1002'}
for tup in tups:   #for循环字典
    print(f'{tup}:{tups[tup]}')
