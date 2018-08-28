#! /usr/bin/python3
# -*- coding:UTF-8 -*-

# if 基本用法
greeting='hello'
if greeting == 'hello':
    student={'小萌': '1001', '小智': '1002', '小强': '1005','小张': '1006'}
    print(f'字典元素个数为：{len(student)}')
    student.clear()
    print(f'字典删除后元素个数为：{len(student)}')

