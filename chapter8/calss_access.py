#! /usr/bin/python3
# -*-coding:UTF-8-*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def info(self):
        print(f'学生：{self.name}；分数: {self.score}')

stu = Student('xiaomeng',95)
print (f'修改前分数：{stu.score}')
stu.info()
stu.score=0
print (f'修改后分数：{stu.score}')
stu.info()
