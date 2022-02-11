def f (n, k):
    if n > k:
        return 0
    elif n == 13 or n == 15:
        return 0
    elif n == k:
        return 1
    return f(n + 1, k) + f(n + 2, k) + f(n * 3, k)
print(f(1, 10) * f(10, 22))