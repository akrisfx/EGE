for a in range(1, 1000):
    ok = 1
    for x in range(1,1000):
        for y in range(1, 1000):
            ok *= int((y + 3*x < a) or (2*y + x > 50) or (4*y - x < 40))
            if not ok: break
        if not ok: break
    if ok: print(a)

# 76