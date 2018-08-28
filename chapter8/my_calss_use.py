#! /usr/bin/python3
# -*-coding:UTF-8-*-

class MyClass(object):
    i = 123    
    def f(self):
        return 'hello world'

use_class = MyClass()
print(f'调用类的属性：{use_class.i}')
print(f'调用类的方法：{use_class.f()}')
