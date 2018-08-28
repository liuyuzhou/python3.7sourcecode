class Animal(object):
    def run(self):
        print('Animal is running...')

    def jump(self):
        print('Animal is jumpping....')

    def __run(self):
        print('I am a private method.')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

print(f'a是否为list类型：{isinstance(a, list)}')
print(f'b是否为Animal类型：{isinstance(b, Animal)}')
print(f'c是否为Dog类型：{isinstance(c, Dog)}')

print(f'c是否为Dog类型：{isinstance(c, Dog)}')
print(f'c是否为Animal类型：{isinstance(c, Animal)}')

b = Animal()
print(f'b是否为Dog类型：{isinstance(b, Dog)}')

