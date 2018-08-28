#! /usr/bin/python3
# -*- coding:UTF-8 -*-
import re

print(re.match(r'^(\d+)(0*)$', '102300').groups())
