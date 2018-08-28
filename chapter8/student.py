#! /usr/bin/python3
# -*- coding:UTF-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

std = Student('xiaozhi', 90)
def info(std):
    print(f'学生：{std.name}；分数: {std.score}')
info(std)
