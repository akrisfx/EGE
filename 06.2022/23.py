def f(n, k):
    if n > k:
        return 0
    # if n == 14:
    #     return 0
    if n == k:
        return 1

    return f(n + 2 , k) + f(n * 2,k)


print(f(1, 100))