#! /usr/bin/python3
# -*- coding:UTF-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

    def __run(self):
        print('I am a private method.')

class Dog(Animal):
    def eat(self):
        print('Eating ...')

class Cat(Animal):
    pass

dog = Dog()
dog.__run()
