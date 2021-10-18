def countOccurrences(str1):
    dict = {}
    list1 = str1.split()

    for word in list1:
        if word not in dict.keys():
            dict[word] = 1
        else:
            dict[word] += 1
    return dict

str1 = "qwe qwe asd asd zxc qwe asd qwe asd zxc zxc zxc"
print(countOccurrences(str1))