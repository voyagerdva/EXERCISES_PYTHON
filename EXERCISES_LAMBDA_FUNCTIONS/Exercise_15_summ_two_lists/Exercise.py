class Operations():
    def listsSumm(self, list1, list2):
        result = list(map(lambda x, y: x + y, list1, list2))
        return result

list1 = [1,2,3]
list2 = [4,5,6]
print(f"\n Original lists:\n{list1}\n{list2}")

oper = Operations()
result = oper.listsSumm(list1, list2)
print(f"\nresult of they summ from class is : {result}")
