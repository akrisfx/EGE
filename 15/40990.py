P = list(range(19, 84 + 1))
Q = list(range(4, 51 + 1))

for a1 in range(1, 500):
    for a2 in range(a1 + 1, a1 + 500):
        ok = 1
        A = list(range(a1, a2 + 1))
        for x in range(1, 1000):
            ok *= int( (x in P) <= ((x not in P) <= (not((x in P) and (x not in A)))) )
            if not ok:
                break
        if ok:
            