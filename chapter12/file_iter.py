#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test.txt'
f_name = open(path)
for line in f_name:
    print(f'line is:{line}')
f_name.close()
