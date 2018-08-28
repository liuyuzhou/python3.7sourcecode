#! /usr/bin/python3
# -*-coding:UTF-8-*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def info(self):
        print(f'学生：{self.__name}；分数: {self.__score}')

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0<=score<=100:
            self.__score = score
        else:
            print('请输入0到100的数字。')

stu = Student('xiaomeng',95)
print(f'修改前分数：{stu.get_score()}')
stu.info()
stu.set_score(-10)
print(f'修改后分数：{stu.get_score()}')
stu.info()
