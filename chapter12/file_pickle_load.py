#! /usr/bin/python
# -*-coding:UTF-8-*-

import pickle

try:
    f_name = open('dump.txt', 'rb')
    print(f'load result:{pickle.load(f_name)}')
finally:
    f_name.close()
