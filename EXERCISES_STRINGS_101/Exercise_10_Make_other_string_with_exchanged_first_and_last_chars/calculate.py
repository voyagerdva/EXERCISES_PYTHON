def makeString(str1):
    str2 = str1[-1:] + str1[1:-1] + str1[:1]
    return str2


str1 = "PkjlkjlkjlkjlO"
print((makeString(str1)))