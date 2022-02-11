count = 0
for i in range(1,1000000):
    d = i
    n = 7
    s = 35
    while s <= 2570:
        s = s + d
        n = n + 9
    if n == 196:
        print(i)
        count += 1
print(count)