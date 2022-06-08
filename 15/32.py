for a in range(1, 1000):
    ok = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            ok *= int((y + 2*x != 99) or (y > a) or (x > a))
            if not ok: break
        if not ok: break
    if ok:
        print(a)