#! /usr/bin/python
# -*-coding:UTF-8-*-

from io import StringIO

io_val = StringIO('Hello\nWorld!\nWelcome!')
while True:
    line = io_val.readline()
    if line == '':
        break
    print(f'line value:{line.strip()}')
