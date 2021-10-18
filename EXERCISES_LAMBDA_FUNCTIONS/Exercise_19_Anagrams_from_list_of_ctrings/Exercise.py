from collections import Counter

anagrams = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = "abcd"

result = list(filter(lambda x: Counter(str) == Counter(x), anagrams))

print(result)
print(Counter(str))