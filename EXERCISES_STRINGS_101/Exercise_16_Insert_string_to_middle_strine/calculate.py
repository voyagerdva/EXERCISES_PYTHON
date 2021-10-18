str1 = "lkjlkjlkjlkj lkjlkjlkjsddlkjlkj  lkjlkj"
strInserted = "-=12321=-"
middle = len(str1) // 2
result = str1[:middle] + strInserted + str1[middle:]

print(result)