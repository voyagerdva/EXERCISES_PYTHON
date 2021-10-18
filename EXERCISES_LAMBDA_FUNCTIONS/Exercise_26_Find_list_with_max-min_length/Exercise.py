list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

def findMax(list1):
    lenMax = len(list1[0])
    listMax = []
    for i in range(1, len(list1)):
        if len(list1[i]) > len(list1[i-1]):
            lenMax = len(list1[i])
            listMax = list1[i]
    return lenMax, listMax

print(findMax(list1))

def findMax2(list1):
    max_length = max(len(x) for x in list1)
    max_list = max(list1, key = lambda x: len(x))
    return max_length, max_list

def findMin2(list1):
    min_length = min(len(x) for x in list1)
    min_list = min(list1, key = lambda x: len(x))
    return min_length, min_list

print(findMax2(list1))

print(findMin2(list1))

# results = list(filter(lambda x: