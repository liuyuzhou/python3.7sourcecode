# !/usr/bin/python
# -*- coding:UTF-8 -*-
import datetime

dt = datetime.datetime.now()
print(f"当前时间：{dt}")
print(f"(%Y-%m-%d %H:%M:%S: {dt.strftime('%Y-%m-%d %H:%M:%S %f')})")
print(f"(%Y-%m-%d %H:%M:%S %p): {dt.strftime('%y-%m-%d %I:%M:%S %p')}")
print(f"%a: {dt.strftime('%a')} ")
print(f"%A: {dt.strftime('%A')} ")
print(f"%b: {dt.strftime('%b')} ")
print(f"%B: {dt.strftime('%B')} ")
print(f"日期时间%c: {dt.strftime('%c')} ")
print(f"日期%x：{dt.strftime('%x')} ")
print(f"时间%X：{dt.strftime('%X')} ")
print(f"今天是这周的第 {dt.strftime('%w')} 天 ")
print(f"今天是今年的第 {dt.strftime('%j')} 天 ")
print(f"这周是今年的第 {dt.strftime('%U')} 周 ")
