#! /usr/bin/python3
# -*-coding:UTF-8-*-

class DefaultInit(object):
    def show(self):
        print ('我是类中定义的方法，需要通过实例化对象调用。')

test = DefaultInit()
print('类实例化结束。')
test.show()
