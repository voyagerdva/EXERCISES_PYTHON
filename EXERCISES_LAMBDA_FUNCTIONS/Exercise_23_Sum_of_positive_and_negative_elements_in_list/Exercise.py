list1 = [2, 4, -6, -9, 11, -12, 14, -5, 17]

resultPositive = sum(list(filter(lambda x: x > 0, list1)))
resultNegative = sum(list(filter(lambda x: x < 0, list1)))

print(resultPositive)
print(resultNegative)