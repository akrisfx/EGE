for a in range(1, 1000):
    ok = 1 
    for x in range(1, 1000):
        ok *= int( (x & 25 != 0) <= ((x & 17 ==0) <= (x & a != 0)) )
        if not ok:
            break
    if ok:
        print(a)
        break