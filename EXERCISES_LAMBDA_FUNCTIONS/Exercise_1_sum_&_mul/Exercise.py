class Lam():
    def __init__(self, n):
        self.n = n

    def summ(self):
        return lambda x : x + self.n

    def multiple(self):
        return lambda x, y : x*y

r = Lam(20)
print(r.summ()(100))
print(r.multiple()(3,4))

