#! /usr/bin/python
# -*-coding:UTF-8-*-
import os

try:
    print(f"remove result:{os.remove('test2.txt')}")
except Exception:
    print('file not found')
