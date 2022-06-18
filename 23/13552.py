def f (n, k):
    if n == k:
        return 1
    elif n > k:
        return 0
    return f(n + 1, k) + f(n + 2, k) + f(n + 4, k)


print(f(1, 8) * f(8, 15))
