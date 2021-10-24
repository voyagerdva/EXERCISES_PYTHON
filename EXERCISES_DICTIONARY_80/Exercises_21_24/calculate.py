##########################  Exercise 21 ####################
print("\n------------------ Exercise 21 - All combinations of letters from diff key in dict ----")

import itertools

d = {'1': ['a', 'b'], '2': ['c', 'd'], '3': ['a', 'b'], '4': ['c', 'd']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))



##########################  Exercise 22 #############################
print("\n------------------ Exercise 22 - 3 valued of corresponding keys in a dict ----")

from heapq import nlargest
my_dict = {'a': 500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

three_largest = nlargest(3, my_dict, key=my_dict.get)
print(*three_largest, sep='   ')



##########################  Exercise 23 #############################
print("\n------------------ Exercise 23 - Combine values in Python list of dicts ----")

from collections import Counter

item_list = [{'item': 'item1', 'amount': 400},
             {'item': 'item2', 'amount': 300},
             {'item': 'item1', 'amount': 750}]
result = Counter()

for d in item_list:
    result[d['item']] += d['amount']

print(result)


##########################  Exercise 24 #############################
print("\n------------------ Exercise 24 - Create dict from string ----")

from collections import defaultdict, Counter
str1 = 'qwertyqweerqwerqweqwq'

d = {}

for letter in str1:
    d[letter] = d.get(letter, 0) +1

print(d)

