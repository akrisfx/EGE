
for i in range(1,10000000):
    s = i
    n = 3
    while s <= 45:
        s += 4
        n *= 3
    if n == 729:
        print(i)