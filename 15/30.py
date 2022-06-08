for a in range(1, 1000):
    ok = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            ok *= int( (y + 2*x < a) or (3*y + 2*x > 120) or (3*y - x > 30) ) 
            if not ok: break
        if not ok: break
    if ok:
        print(a)
        break
# 118