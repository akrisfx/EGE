for i in range(1, 10000000):
    x = i
    a = 0
    b = 0
    while x > 0:
        if x % 2 == 1:
            a = a + 1
        else:
            b = b + 1
        x = x // 10
    if a == 1 and b == 4:
        print(i)
