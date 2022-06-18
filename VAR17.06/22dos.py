for i in range(1, 100000):
    x = i
    l = 0
    m = 0
    while x > 0:
        m = m + 1
        if x % 2 == 0:
            l = l + x % 8
        x = x // 8
    if l == 12 and m == 3:
        print(i)