class Animal(object):
    def run(self):
        print('Animal is running...')

    def jump(self):
        print('Animal is jumpping....')

    def __run(self):
        print('I am a private method.')

class Dog(Animal):
    def eat(self):
        print('Eating ...')

class Cat(Animal):
    pass

dog = Dog()
dog.run()
dog.jump()

cat = Cat()
cat.run()
cat.jump()
