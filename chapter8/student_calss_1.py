#! /usr/bin/python3
# -*-coding:UTF-8-*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def info(self):
        print(f'学生：{self.__name}；分数: {self.__score}')

stu = Student('xiaomeng',95)
print(f'修改前分数：{stu.__score}')
stu.info()
stu.__score = 0
print(f'修改后分数：{stu.__score}')
stu.info()
