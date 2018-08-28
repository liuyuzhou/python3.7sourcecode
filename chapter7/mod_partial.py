#! /usr/bin/python3
# -*- coding:UTF-8 -*-

from functools import partial

def mod_partial(n, m):
  return n % m

mod_by_100 = partial(mod_partial, 100)

print(f'自定义函数，100对7取余结果为：{mod_partial(100, 7)}')
print(f'调用偏函数，100对7取余结果为：{mod_by_100(7)}')
