
for a in range(1, 10000):
    ok = 1
    for x in range(1, 10000):
        ok *= int( (x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0)) )
        if not ok:
            break
    if ok:
        print(a)
        break