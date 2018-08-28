#! /usr/bin/python
# -*-coding:UTF-8-*-

import json

data = { 'num': 1002, 'name': 'xiao zhi'}
json_str = json.dumps(data)
print(f"Python 原始数据：{data}")
print(f"JSON 对象：{json_str}")
