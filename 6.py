count = 0
for i in range(1, 10000):
    s = i
    s = 5 * (s // 7)
    n = 1
    while s < 500:
        s = s + 15
        n = n * 2
    if n == 512:
        count += 1
        print(i)
print(count)