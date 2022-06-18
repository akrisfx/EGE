for i in range(1, 100000000000000):
    s = i
    s = s // 5
    n = 1
    k = 3
    while s > k:
        s -= k
        k *= 3
        n += 5
    if n == 51:
        print(i)

