from functools import reduce

class Operations():
    def rearrange(self, list1):
        return sorted(list1, key = lambda i: 0 if i == 0 else -1 / i)

oper = Operations()

list1 = [-1, 2, -3, 5, 7, 8, 9, -10]
print(f"\n Original arrays: \n{list1}")

print(f"\n Rearranged list: {oper.rearrange(list1)}")