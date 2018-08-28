#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def func_count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = func_count()
print(f'f1的结果是：{f1()}')
print(f'f2的结果是：{f2()}')
print(f'f3的结果是：{f3()}')
