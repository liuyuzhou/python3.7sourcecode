class Student(object):

    def __init__(self):
        self.name = 'xiaozhi'

    def __getattr__(self, attr):
        if attr=='score':
            return 95

stu = Student()
print((stu.name))
print((stu.score))