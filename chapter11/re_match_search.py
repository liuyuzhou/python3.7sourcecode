#! /usr/bin/python3
# -*- coding:UTF-8 -*-

import re

line = 'Cats are smarter than dogs'

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
   print(f'use match,the match string is: {matchObj.group()}')
else:
   print("No match string!!")

matchObj = re.search( r'dogs', line, re.M | re.I)
if matchObj:
   print(f'use search,the match string is: {matchObj.group()}')
else:
   print("No match string!!")
