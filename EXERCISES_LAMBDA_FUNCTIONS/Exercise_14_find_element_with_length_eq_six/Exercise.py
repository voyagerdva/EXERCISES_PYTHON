class Operations():
    def find_six(self, weekdays):
        result = list(filter(lambda day: day if len(day) == 6 else '', weekdays))
        return result

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(f"\n Original list is : {weekdays}")

fi = Operations()
result = fi.find_six(weekdays)
print(result)

#==============================================================================================

result1 = []
def find_six(weekdays):
    for day in weekdays:
        if len(day) == 6:
           result1.append(day)

find_six(weekdays)
print("\n", result1)