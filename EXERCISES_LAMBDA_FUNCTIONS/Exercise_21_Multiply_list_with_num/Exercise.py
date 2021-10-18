list1 = [2,4,6,9,11]
N = 2

result = list(map(lambda x: x*N, list1))

print(result)
print(" ".join(map(str, result)))