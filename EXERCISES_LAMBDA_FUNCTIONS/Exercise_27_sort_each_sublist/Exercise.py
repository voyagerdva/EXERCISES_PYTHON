list1 = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]

result = list(sorted(x, key = lambda x: x[0]) for x in list1)

print(result)