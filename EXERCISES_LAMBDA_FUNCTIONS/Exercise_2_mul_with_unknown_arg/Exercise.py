class Lam():
    def mul(self, n):
        return lambda x : x*n

ins = Lam()
result = ins.mul(100)

print(result(15))



