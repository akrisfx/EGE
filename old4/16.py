def f(n):
    if n == 0:
        return 0
    elif n > 0 and n & 1 == 0:
        return f(n // 2)
    elif n & 1 == 1:
        return 1 + f(n - 1)

for i in range(1, 10000):
    if f(i) == 12:
        print(i)