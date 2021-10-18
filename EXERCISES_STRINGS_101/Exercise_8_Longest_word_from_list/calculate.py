def longestWord(list):
    length = 0
    position = 0
    word = ""
    for i in range(len(list)):
        if len(list[i]) > length:
            length = len(list[i])
            word = list[i]

    return word, length

list = ["qwe", "qwert", "qwertyu", "qwert", "aa", "sdfsdfsdfsdfsdf", "s", "d", ""]

print(longestWord(list))