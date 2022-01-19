for i in range(9999, 30000):
    x = i
    a = 0
    b = 0
    while x > 0:
        y = x % 10
        if y > 4:
            a = a + 1
        if y < 6:
            b += 1
        x = x // 10
    if (a == 3 and b == 4):
        print(i, a, b)
    