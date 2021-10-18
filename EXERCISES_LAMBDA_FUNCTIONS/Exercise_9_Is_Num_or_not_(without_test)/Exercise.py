class Operations():
    def is_num(self):
        return lambda x: x.replace('.','',1).isdigit()
    # def is_num1(self):
    #     return lambda x: x.replace('.','',1).isdigit()

oper = Operations()

print(oper.is_num()("26587"))
print(oper.is_num()("2.6587"))
print(oper.is_num()("-26587"))
print(oper.is_num()("00"))
print(oper.is_num()("A001"))
print(oper.is_num()("001"))

print("\n Checking numbers: ")
is_num1 = lambda r: oper.is_num()(r[1:]) if r[0] == '-' else oper.is_num()(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))