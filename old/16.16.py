import sys

sys.setrecursionlimit(214748355)

def f(n):
    if n > 0 and n % 5 == 0:
        b =  n + f(n - 5)
        return(b)
    elif n % 5 > 0:
        a = n % 2 + int(f(n - 2))
        return int(a)
    elif n == 0:
        return 0

print(f(79))