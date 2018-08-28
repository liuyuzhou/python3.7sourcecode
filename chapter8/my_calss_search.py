#! /usr/bin/python3
# -*-coding:UTF-8-*-

class MyClass(object):
    i = 123
    def __init__(self, name):
        self.name = name

    def f(self):
        return 'hello,'+ self.name

use_class = MyClass('xiaomeng')
print(f'调用类的属性：{use_class.i}')
print(f'调用类的方法：{use_class.f()}')

# use_class = MyClass()
