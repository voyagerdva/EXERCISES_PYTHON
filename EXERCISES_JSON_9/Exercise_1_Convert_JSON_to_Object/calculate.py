import json

json_obj = '{ "Name":"David", "Class":"I", "Age":6}'

python_obj = json.loads(json_obj)

print("\nJSON data:")
print(python_obj)
print("\nName: ", python_obj["Name"])
print("\nClass: ", python_obj["Class"])
print("\nAge: ", python_obj["Age"])