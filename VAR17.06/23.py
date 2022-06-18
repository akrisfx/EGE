def f(n, m):
    if n == m:
        return 1
    elif n > m:
        return 0
    return f(n + 1, m) + f(n + 2, m)

print(f(3, 18))