from functools import reduce

class Operations():
    def intersection(self, array_nums_1, array_nums_2):
        return list(filter(lambda x: x in array_nums_1, array_nums_2))

oper = Operations()

array_nums_1 = [1,2,3,4,5,6,7,8,9,10]
array_nums_2 = [1,2,4,8,9]

print(f"\n Original arrays: \n{array_nums_1}, \n{array_nums_2}")

print(f"\n result is: {oper.intersection(array_nums_1, array_nums_2)}")