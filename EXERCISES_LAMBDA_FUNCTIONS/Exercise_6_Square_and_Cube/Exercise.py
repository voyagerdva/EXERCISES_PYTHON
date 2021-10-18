
class Operations():

    def squareNums(self, nums):
        return list(map(lambda x: x ** 2, nums))

    def cubeNums(self, nums):
        return list(map(lambda x: x ** 3, nums))

oper = Operations()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\nOriginal list of integer:\n {nums}")

square = oper.squareNums(nums)
print(f"\nSquare integers :\n {square}")

cube = oper.cubeNums(nums)
print(f"\nCube integers :\n {cube}")
