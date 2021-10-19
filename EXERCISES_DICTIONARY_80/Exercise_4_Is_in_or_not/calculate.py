
def is_key_present(x, d1):
    if x in d1:
        print(f"{x} in dict")
    else:
        print(f"{x} not in dict")

d = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

is_key_present(5, d)
is_key_present(9, d)