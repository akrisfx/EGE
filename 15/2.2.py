P = list(range(10 + 1, 15))
Q = list(range(5, 20 + 1))
R = list(range(15, 25 + 1))

for a1 in range(2, 20 + 1):
    for a2 in range(a1 + 1, 25 + 1):
        ok = 1
        A = list(range(a1, a2 + 1))
        for x in range(1, 1000):
            ok *= int( ((x not in A) <= (x in P)) != ((x in Q) <= (x in R)) )
            if not ok:
                break
        if ok and (a1 == 7 or a1 == 2 or a1 == 5 or a1 == 20):
            print(a1, a2)

# 3) [5;3]
            