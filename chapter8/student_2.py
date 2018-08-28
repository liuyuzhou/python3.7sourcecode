#! /usr/bin/python3
# -*- coding:UTF-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'学生名称: {self.name}'

print(Student('xiaozhi'))
