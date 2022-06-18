def f(m, n, a):
    return int((2*m + 3*n > 43) or (m < a) or (n <= a))


for a in range(0, 1000):
    ok = 1
    for m in range(0, 1000):
        for n in range(0, 1000):
            ok *= f(m, n, a)
            if not ok:
                break
    if ok:
        print(a)
