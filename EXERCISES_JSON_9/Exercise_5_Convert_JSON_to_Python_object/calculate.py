import json

jobj_dict = '{"name": "David", "Age": 6, "class": "IV"}'
jobj_list = '["Red", "Green", "Black"]'
jobj_string = '"Python Json"'
jobj_int = '1234'
jobj_float = '21.34'

python_dict = json.loads(jobj_dict)
print("\njobj_dict: ", jobj_dict)
print("Python dict: ", python_dict)

python_list = json.loads(jobj_list)
print("\njobj_list: ", jobj_list)
print("Python list: ", python_list)

python_string = json.loads(jobj_string)
print("\njobj_string: ", jobj_string)
print("Python string: ", python_string)

python_int = json.loads(jobj_int)
print("\njobj_int: ", jobj_int)
print("Python int: ", python_int)

python_float = json.loads(jobj_float)
print("\njobj_float: ", jobj_float)
print("Python float: ", python_float)
