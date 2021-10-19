d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}

d4 = {}

print(f"\n{d1}\n{d2}\n{d3}")

for d in (d1, d2, d3): d4.update(d)
print(f"\n{d4}")