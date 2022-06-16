for i in range(10000, 10000000):
    s = i
    s = (s - 10) // 7
    n = 1
    while s > 0:
        n = n * 2
        s = s - n
    if n == 1024:
        print(i)