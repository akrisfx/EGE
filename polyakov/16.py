def f(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    elif n >= 2 and n & 1 == 0:
        return f(n//2) + 1
    elif n >= 2 and n & 1 == 1:
        return f(n - 1) + n

for i in range(1, 1000):
    go = f(i)
    if go == 19:
        print(i, go)
