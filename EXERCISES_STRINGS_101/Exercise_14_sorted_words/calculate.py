def sortedList(str1):
    words = [word for word in str1.split(",")]
    print(words)

    wordsSorted = ", ".join(sorted(list(set(words))))
    return wordsSorted

str1 = "asfd,bcd,dll,lkj,ass,dsd,cad"
print(sortedList(str1))