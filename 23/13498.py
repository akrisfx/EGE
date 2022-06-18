def f(n, k):
    if n == k:
        return 1
    elif n > k:
        return 0
    return f(n + 1, k) + f(n + 3, k)


print(f(1, 9) * f(9, 17))
