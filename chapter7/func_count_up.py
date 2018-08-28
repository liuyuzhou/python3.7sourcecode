#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def func_count_up():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = func_count_up()
print(f'f1的结果是：{f1()}')
print(f'f2的结果是：{f2()}')
print(f'f3的结果是：{f3()}')
