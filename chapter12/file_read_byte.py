#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test.txt'
f_name = open(path, 'w')
print(f"write length:{f_name.write('Hello')}")
f_name = open(path)
c_str = f_name.read(1)
while c_str:
    print(f'read str is:{c_str}')
    c_str = f_name.read(1)
f_name.close()
