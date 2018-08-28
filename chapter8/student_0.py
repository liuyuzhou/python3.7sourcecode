#! /usr/bin/python3
# -*- coding:UTF-8 -*-

class Student0(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def info(self):
        print(f'学生：{self.name}；分数: {self.score}')

stu = Student0('xiaomeng', 95)
stu.info()
