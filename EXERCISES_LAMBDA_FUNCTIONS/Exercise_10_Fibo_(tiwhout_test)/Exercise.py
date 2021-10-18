from functools import reduce

class Operations():
    def fibo(self):
        return lambda n: reduce(lambda x, _: x +[x[-1]+x[-2]], range(n-2), [0,1])

oper = Operations()

print(f"\n Fibo series up to 2: {oper.fibo()(2)}")
print(f"\n Fibo series up to 2: {oper.fibo()(5)}")
print(f"\n Fibo series up to 2: {oper.fibo()(6)}")
print(f"\n Fibo series up to 2: {oper.fibo()(100)}")
