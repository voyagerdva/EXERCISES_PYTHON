
class Operations():
    def count_even(self, list1):
        return len(list(filter(lambda x: (x%2 == 0), list1)))
    def count_odd(self, list1):
        return len(list(filter(lambda x: (x%2 != 0), list1)))

oper = Operations()

list1 = [1,2,3,4,5,6,7,8,9,11, 15]
print(f"\n Original arrays: \n{list1}")

print(f"\n Even nums quantity in list: {oper.count_even(list1)}")
print(f"\n Odd nums quantity in list: {oper.count_odd(list1)}")