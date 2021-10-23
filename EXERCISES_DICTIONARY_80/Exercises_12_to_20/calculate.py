##########  exrcs 12 #############################
print("\n------------------ Exercise 12 - remove one item from dict ----------------------------")
myDict = {'a':1,'b':2,'c':3,'d':4}

print(myDict)

if "a" in myDict:
    del myDict["a"]

print(myDict)

######### exrcs 13 ################################
print("\n------------------ Exercise 13 - concatenate two lists to one dict ----------------------------")

keys = ["red", "green", "blue"]
values = ["#FF0000", "#008000", "#0000FF"]

colorDict = dict(zip(keys, values))

print(colorDict)

######### exrcs 14 ################################
print("\n------------------ Exercise 14 - sort dict by key ----------------------------")
color_dict = {'3-red':'#FF0000',
          '2-green':'#008000',
          '1-black':'#000000',
          '4-white':'#FFFFFF'}
print(*color_dict, sep="\n")
print("")
for key in sorted(color_dict):
    print(f"{key}: {color_dict[key]}")

######### exrcs 15 ################################
print("\n------------------ Exercise 15 - find max and min value from dict ----------------------------")

my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print(my_dict[key_max], my_dict[key_min])


######### exrcs 16 ################################
print("\n------------------ Exercise 16 - get dict from object's fields ----------------------------")

class dictObj(object):
    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'
        self.z = 'Green'

    def do_nothing(self):
        pass

inst = dictObj()
print(inst.__dict__)

######### exrcs 17 ################################
print("\n------------------ Exercise 17 - Remove duplicate from dict ----------------------------")

student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}

result = {}
print(*student_data.items(), sep="\n")

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print("\n", result, sep="\n")


######### exrcs 18 ################################
print("\n------------------ Exercise 18 - dict is empty or not ----------------------------")

d1 = {'x':500, 'y':5874, 'z': 560}
d2 = {}

for dic in d1, d2:
    if bool(dic):
        print(f"Dict {dic} is not empty")
    else:
        print(f"Dict {dic} is empty")

######### exrcs 19 ################################
print("\n------------------ Exercise 19 - combine two dict with adding common values by keys ----------------------------")
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3 = Counter(d1) + Counter(d2)

print(d3)

######### exrcs 20 ################################
print("\n------------------ Exercise 20 - print all unuque values in dict ----------------------------")

L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print(f"\nOriginal dict is {L}")

uniq_values = set(val for dic in L for val in dic.values())
print(f"\nUniqut values are {uniq_values}")




