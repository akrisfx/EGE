import matplotlib.pyplot as plt
from functools import lru_cache


@lru_cache(maxsize=000000)
def f(n):
    if n == 0:
        return 0
    elif n % 7 != 0:
        return f(n - 1) + 1
    else:
        return f(n / 7)


maxx = 0
# print(f(35_000_000_000 - 500000))
# for i in range(35_000_000_000 - 100_000, 35_000_000_000):
#     ss = f(i)
#     if ss > maxx:
#         maxx = ss
#         print(maxx, i)

for i in range(1, 1000):
    print(i, f(i))

