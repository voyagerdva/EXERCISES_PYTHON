
class Operations():

    def filterEven(self, nums):
        return list(filter(lambda x: x%2 == 0, nums))

    def filterOdd(self, nums):
        return list(filter(lambda x: x%2 != 0, nums))

    def filterNegative(self, nums):
        return list(filter(lambda x: x < 0, nums))

oper = Operations()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\nOriginal list of integer:\n {nums}")

even = oper.filterEven(nums)
print(f"\nEven integers :\n {even}")

odd = oper.filterOdd(nums)
print(f"\nOdd integers :\n {odd}")

nums = range(-5, 5)
negative = oper.filterNegative(nums)
print(f"\nNegative integers :\n {negative}")

# Output: [-5, -4, -3, -2, -1]