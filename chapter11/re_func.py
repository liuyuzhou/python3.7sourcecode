#! /usr/bin/python3
# -*- coding:UTF-8 -*-
import re

pt = re.compile(r'(w+) (w+)')
greeting = 'i say, hello world!'

print(pt.sub(r'2 1', greeting))


def func(m):
    return m.group(1).title()+' '+m.group(2).title()

print(pt.sub(func, greeting))
