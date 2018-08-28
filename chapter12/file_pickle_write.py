#! /usr/bin/python
# -*-coding:UTF-8-*-

import pickle

try:
    d = dict(name='xiao zhi', num=1002)
    f_name = open('dump.txt', 'wb')
    pickle.dump(d, f_name)
finally:
    f_name.close()

