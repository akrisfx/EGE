for a in range(1, 1000):
    ok = 1
    for x in range(0,1000):
        for y in range(0, 1000):
            ok *= int( ((x <= 9) <= (x*x <= a)) and ((y*y <= a) <= (y <= 9)) )
            if not ok:
                break
        if not ok:
            break
    if ok: print(a)

# 99