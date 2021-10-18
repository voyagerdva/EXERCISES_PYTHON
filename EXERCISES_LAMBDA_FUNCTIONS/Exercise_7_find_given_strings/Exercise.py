
class Operations():

    def findPrefix(self, x):
        return lambda x:True if x.startswith("P") else False

oper = Operations()

print(oper.findPrefix("Python")("Python"))
print(oper.findPrefix("Java")("Java"))
