d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
summ_ke = 0
summ_va = 0

for ke, va in d.items():
    summ_ke += ke
    summ_va += va

print(summ_ke, summ_va)

print(sum(d.values()))
print(sum(d.keys()))