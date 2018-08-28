#! /usr/bin/python3
#-*- coding:UTF-8 -*-

for letter in 'hello':       #示例1 
   if letter == 'l':
      break
   print (f'当前字母为:{letter}')

num = 10                   #示例2
while num > 0:
   print (f'输出数字为:{num}')
   num -= 1
   if num == 8:
      break
