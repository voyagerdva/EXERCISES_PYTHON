d = {'a': 100, 'b': 200}
print(d.keys())
print(d.items())

for ke, va in ('a', 100), ('b', 200), ('c', 100), ('d', 200):
    print(f"\n{ke} correspond to {va}")

for ke, va in d.items():
    print(f"\n{ke} correspond to {va}")
