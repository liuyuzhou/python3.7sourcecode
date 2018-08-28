#! /usr/bin/python3
# -*- coding:UTF-8 -*-

num = 10
if num <= 10:
    if num>=5:
        print('num的值介于5到10之间')
    else:
        print('num的值不介于5到10之间')
else:
    print('num的值不介于5到10之间')

# 简洁写法方式一
if 5<=num and num <= 10:
    print('num的值介于5到10之间')
else:
    print('num的值不介于5到10之间')

# 简洁写法方式二
if 5 <= num <= 10:
    print('num的值介于5到10之间')
else:
    print('num的值不介于5到10之间')

