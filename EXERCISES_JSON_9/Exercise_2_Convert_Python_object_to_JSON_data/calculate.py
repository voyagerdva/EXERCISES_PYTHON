import json

# a Python object dict:
python_obj = {
    "name": "David",
    "class": "IV",
    "age": 6
}

print(type(python_obj))

# convert into JSON:
j_data = json.dumps(python_obj)

# result is a JSON string:
print(j_data)
print(type(j_data))