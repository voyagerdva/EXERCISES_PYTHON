list1 = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
list1 = list(filter(lambda item: item[0].isupper() and item[1].islower(), list1))

result = len("".join(list1))
print(result)