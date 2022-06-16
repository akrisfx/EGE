def d(n, m):
    return n % m == 0

for a in range(1,1000):
    ok = 1
    for x in range(1, 1000):
        ok *= int( (not(d(x, 15)) or not(d(x, 28)) or d(x, a)) and (a > 70) )
        if not ok:
            break
    if ok:
        print(a)