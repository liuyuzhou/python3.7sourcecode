class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f'名称：{self.name}')

stu = Student('xiaomeng')
print(stu())
print(callable(Student('xiaozhi')))