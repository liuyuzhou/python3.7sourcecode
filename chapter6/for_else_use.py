#! /usr/bin/python3
#-*- coding:UTF-8 -*-

names = ['xiaomeng', 'xiaozhi']
for name in names:
    if name == "xiao":
        print(f"名称：{name}")
        break
    print(f"循环名称列表 {name}")
else:
    print("没有循环数据!")
print("结束循环!")
