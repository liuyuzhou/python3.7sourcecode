#! /usr/bin/python3
# -*- coding:UTF-8 -*-

total_val = 0  # 这是一个全局变量
def sum_num(arg1, arg2):
    total_val = arg1 + arg2  # total_val在这里是局部变量.
    print (f"函数内是局部变量:{total_val}")
    return total_val

def total_print():
    print(f'total的值是:{total_val}')
    return total_val

print(f'函数求和结果:{sum_num(10, 20)}')
total_print()
print (f"函数外是全局变量:{total_val}")