from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    elif n & 1 == 0 and n > 1:
        return n * f(n - 1)
    elif n > 1 and n & 1 == 1:
        return 1 + f(n - 2)
print(f(84))