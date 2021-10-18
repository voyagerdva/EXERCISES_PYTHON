str1 = "Python"
result = ""
if len(str1) > 2:
    for i in range(4):
        result = result + str1[-2:]

print(result)