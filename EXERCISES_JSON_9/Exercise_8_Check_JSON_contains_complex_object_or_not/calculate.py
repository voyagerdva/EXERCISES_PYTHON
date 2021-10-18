import json

def is_compltx_num(objct):
    if "__complex__" in objct:
        return  complex(objct["real"], objct["img"])
    return objct

complex_object = json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook=is_compltx_num)
simple_object = json.loads('{"real": 4, "img": 3}', object_hook=is_compltx_num)

print("Complex_object: ", complex_object)
print("Without complex_object: ", simple_object)
