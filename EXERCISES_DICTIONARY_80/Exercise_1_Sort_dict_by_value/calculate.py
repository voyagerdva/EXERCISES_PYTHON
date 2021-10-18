import operator

d = {1:2, 3:4, 4:3, 2:1, 0:0}
print("Original dict: ", d)

sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print(f"List of Dict in ascending order by value: {sorted_d}")

sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(f"Dict in descending order by value: {sorted_d}")