list1 = ['Python', 3, 2, 4, 5, 'version']

result = max(list1, key=lambda x: (isinstance(x, int), x))


print(result)