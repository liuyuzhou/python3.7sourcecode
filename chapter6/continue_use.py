#! /usr/bin/python3
#-*- coding:UTF-8 -*-

for letter in 'hello':     # 示例1
   if letter == 'l':
      continue
   print(f'当前字母 :{letter}')

num = 3                    # 示例2
while num > 0:              
   num -= 1
   if num == 2:
      continue
   print(f'当前变量值 :{num}')
