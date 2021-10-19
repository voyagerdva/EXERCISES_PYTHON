d1 = {1:10, 2:20, 3:30}
d2 = {4:40, 5:50, 6:60}

d3 = {}

for i in (d1, d2):
    print(i)
    d3.update(i)

print(d3)

d4 = d1.copy()
d4.update(d2)

print(d4)