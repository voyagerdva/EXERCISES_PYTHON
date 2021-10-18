def rearrange_bigger(n):
    """ Break the number into digits and store each in a list """

    digits = list(str(n))

    for i in range(len(digits)-2, -1, -1):
        if digits[i] < digits[i+1]:
            z = digits[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            digits[i:] = [y] + z
            return int("".join(digits))
    return False


n = 12
print(rearrange_bigger(n))
n = 10
print(rearrange_bigger(n))
n = 19
print(rearrange_bigger(n))
n = 47
print(rearrange_bigger(n))
n = 120
print(rearrange_bigger(n))
n = 141
print(rearrange_bigger(n))
n = 507
print(rearrange_bigger(n))