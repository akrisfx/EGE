P = list(range(25, 50 + 1))
Q = list(range(32, 47 + 1))
arr = []

for a1 in range(1, 100):
    for a2 in range(a1 + 1, 105):
        ok = 1
        A = list(range(a1, a2 + 1))
        for x in range(1, 1000):
            ok *= int( ((x not in A) <= (x in P)) <= ((x not in A) or (x in Q)) )
            if not ok:
                break
        if ok:
            razn = a2 - a1
            arr.append(razn)
            print(razn, a1, a2, A)

print(max(arr))