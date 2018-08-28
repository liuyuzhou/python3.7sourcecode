#! /usr/bin/python
# -*-coding:UTF-8-*-

import fileinput

path = './test.txt'
for line in fileinput.input(path):
    print(f'line is:{line}')
