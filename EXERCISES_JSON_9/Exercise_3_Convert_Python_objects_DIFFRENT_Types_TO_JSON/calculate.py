import json


python_dict = {"name":"Dadid", "age": 6, "class": "IV"}
python_list = ["red", "green", "black"]
python_str = "Python Json"
python_int = (12345)
python_float = (21.34)
python_T = (True)
python_F = (False)
python_N = (None)

json_dict = json.dumps(python_dict)
print("python_dict: ", python_dict)
print("json dict: ", json_dict)

json_list = json.dumps(python_list)
print("python_list: ", python_list)
print("json list: ", json_list)

json_str = json.dumps(python_str)
print("python_str: ", python_str)
print("json str: ", json_str)

json_int = json.dumps(python_int)
print("python_int: ", python_int)
print("json int: ", json_int)

json_float = json.dumps(python_float)
print("python_float: ", python_float)
print("json float: ", json_float)

json_T = json.dumps(python_T)
print("python_T: ", python_T)
print("json T: ", json_T)

json_F = json.dumps(python_F)
print("python_F: ", python_F)
print("json F: ", json_F)

json_N = json.dumps(python_N)
print("python_N: ", python_N)
print("json N: ", json_N)

