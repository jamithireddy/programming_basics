def sum_int(a):
    x = 0
    length = len(a)
    for i in range(length):
        if type(a[i]) == int or type(a[i]) == float:
            x = x + a[i]
        else:
            continue
    return x


p = (2, 4.5, "s", 56, "sha")

r = sum_int(p)
print(r)
