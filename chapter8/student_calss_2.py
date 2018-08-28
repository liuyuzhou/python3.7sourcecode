#! /usr/bin/python3
# -*-coding:UTF-8-*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def info(self):
        print('学生：%s；分数: %s' % (self.__name, self.__score))

    def get_score(self):
        return self.__score

stu = Student('xiaomeng',95)
print(f'修改前分数：{stu.get_score()}')
stu.info()
print(f'修改后分数：{stu.get_score()}')
stu.info()
