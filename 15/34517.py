for a in range(1, 1000000):
    ok = 1
    for x in range(1, 10000000):
        ok *= int( (x & a != 0) <= ((x & 10 == 0) <= (x & 3 != 0)) )
        if not ok:
            break
    if ok:
        print(a)