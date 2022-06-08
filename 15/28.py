
for n in range(1, 10000):
    if sum(
        ((not (70 <= x <= 90)) <= (40 <= x <= 60)) and ((not ( 0 <= x <= n)) <= (70 <= x <= 90)) for x in range(1000)
    ) > 30:
        print(n)
        break
# 49