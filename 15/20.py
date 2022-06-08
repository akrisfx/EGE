def d(n, m):
    return n % m == 0

for a in range(1, 1000):
    ok = 1
    for x in range(1, 1000):
        ok *= int(d(x, a) <= ( d(x, 21) or d(x, 35) ))
        if not ok:
            break
    if ok:
        print(a)
        break

# 21