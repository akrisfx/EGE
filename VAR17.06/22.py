for i in range(1, 10000000):
    x = i
    a = 1
    b = 0
    while x > 0:
        d = x % 7
        a *= d
        if d < 3:
            b += 1
        x //= 7
    if a == 5 and b == 4:
        print(i)
