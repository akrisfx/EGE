P = list(range(10, 25 + 1))
Q = list(range(15, 30 + 1))
R = list(range(25, 40 + 1))

for a1 in range(0, 26):
    for a2 in range(a1 + 1, 41):
        ok = 0
        A = list(range(a1, a2+1))
        for x in range(1,1000):
            # shit = int( ((15 <= x <= 30) <= (x > 40 and x < 25)) and (a1 <= x <= a2) and (x > 25 and x < 10) )
            shit = int( ((x in Q) <= (x not in R)) and (x in A) and (x not in P) )
            ok += shit
            # print(a1, a2, x, ok, shit)
            if ok > 0:
                break
        if ok == 0:
            print(a1, a2)