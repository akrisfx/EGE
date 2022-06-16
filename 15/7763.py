P = list(range(5, 30 + 1))
Q = list(range(14, 23 + 1))
arr = []

for a1 in range(1, 100):
    for a2 in range(a1 + 1, 105):
        ok = 1
        A = list(range(a1, a2 ))
        for x in range(1, 1000):
            if (a1 == 5 and a2 == 13) or (a1 == 5 and a2 == 14):
                a = 0
            ok *= int( ((x in P) == (x in Q)) <= (x not in A) )
            if not ok:
                break
        if ok:
            razn = a2 - a1
            arr.append(razn)
            print(razn, a1, a2, A)

print(arr)
print(max(arr))

# 9
