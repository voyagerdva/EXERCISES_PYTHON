list1 = [[2], [0], [3, 1], [7, 1], [9, 11, 22], [15, 13, 17, 2, 11]]

result = list(sorted(list1, key=lambda l: (len(l), l.sort())))

print(result)