#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test.txt'
f_name = open(path, 'w')
f_name.write('Hello world!\n')
f_name = open(path, 'a')
f_name.write('welcome!')
f_name = open(path,'r')
print(f'readline result:{f_name.readline()}')
print(f'readline result:{f_name.readlines()}')
