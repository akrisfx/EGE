for a in range(1, 1000):
    ok = 1
    for x in range (1, 10000):
        ok *= (x & 125 != 1) or ((x & 34 == 2) <= (x & a == 0))
        if not ok: break
    if ok: print(a)
# 4

for i in range(1,10):
    if i == 5:
        continue
    else: print(i)
