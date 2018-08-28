#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test.txt'
f_name = open(path)
while True:
    c_str = f_name.read(1)
    if not c_str:
        break
    print(f'read str is:{c_str}')
f_name.close()
