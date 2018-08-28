#! /usr/bin/python
# -*-coding:UTF-8-*-

import json

data = { 'num': 1002, 'name': 'xiao zhi'}

json_str = json.dumps(data)
print(f"Python 原始数据：{data}")
print(f"JSON 对象：{json_str}")

data2 = json.loads(json_str)
print (f"data2['name']: {data2['name']}")
print (f"data2['num']: {data2['num']}")
