
from functools import lru_cache


# @lru_cache(None)
def f(a, b):
    if a == 0:
        return b
    else:
        return f(a//10, 10*b + a%10)




print(f(4623618421,0))

for i in range(4623610000, 10000000000000000000000000):
    if i % 100000 == 0:
        print(i)
    if f(i, 0) == 1248163264:
        print('| -------------------------------------- |',i)
