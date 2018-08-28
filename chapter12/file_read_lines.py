#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test.txt'
f_name = open(path, 'w')
str_list = ['Hello world!\n', 'welcome!\n', 'welcome!\n']
print(f'write length:{f_name.writelines(str_list)}')
f_name = open(path,'r')
print(f'read result:{f_name.read()}')
f_name = open(path,'r')
print(f'readline result:{f_name.readlines()}')
