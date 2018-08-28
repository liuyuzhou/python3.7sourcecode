class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

fib = Fib()
print(fib[3])
print(fib[10])