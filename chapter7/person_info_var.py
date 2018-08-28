#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def person_info_var(arg,*vartuple):
    print(arg)
    for var in vartuple:
        print(f'我属于不定长参数部分:{var}')
    return

print('------------不带可变参数------------------')
person_info_var('小萌')
print('------------带两个可变参数------------------')
person_info_var('小萌', 21, 'beijing')
print('------------带5个可变参数----------------')
person_info_var('小萌', 21, 'beijing', 123, 'shanghai', 'happy')
