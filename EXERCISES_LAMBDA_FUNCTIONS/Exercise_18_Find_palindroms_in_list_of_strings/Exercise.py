list1 = ["php", "w3r", "Python", "abcd", "Java", "aaa"]

list2 = list(filter(lambda x: x == x[::-1], list1))
list3 = list(filter(lambda x: x == "".join(reversed(x)), list1))

#
# for item in list1:
#     print(item)
#     print(item[::-1])


print(list2)
print(list3)