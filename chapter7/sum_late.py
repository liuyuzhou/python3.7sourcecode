#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def sum_late(*args):
    def calc_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return calc_sum

print(f'调用sum_late的结果：{sum_late(1, 2, 3, 4)}')
calc_sum=sum_late(1, 2, 3, 4)
print(f'调用calc_sum的结果：{calc_sum()}')
