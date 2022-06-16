def per(num, base):
    new = ''
    while num > 0:
        new += str(num % base)
        num = num // base
    return new[::-1]

print(per(5, 2))