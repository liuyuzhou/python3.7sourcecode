#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def person_info(age,name):
    print(f'年龄：{age}')
    print(f'名称：{name}')
    return

print('-------按参数顺序传入参数-------')
person_info(21,'小萌')
print('-------不按参数顺序传入参数，指定参数名-------')
person_info(name='小萌',age=21)
print('-------按参数顺序传入参数，并指定参数名-------')
person_info(age=21,name='小萌')
