import datetime

class Operations():
    def extractYear(self):
        return lambda x: x.year
    def extractMonth(self):
        return lambda x: x.month
    def extractDay(self):
        return lambda x: x.day
    def extractTime(self):
        return lambda x: x.time()

oper = Operations()
now = datetime.datetime.now()

print(now)

year = oper.extractYear()(now)
print(year)
month = oper.extractMonth()(now)
print(month)
day = oper.extractDay()(now)
print(day)
time = oper.extractTime()(now)
print(time)
