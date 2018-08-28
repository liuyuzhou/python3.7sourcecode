#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test.txt'
f_name = open(path)
while True:
    line = f_name.readline(1)
    if not line:
        break
    print(f'read line is:{line}')
f_name.close()
