def f(n):
    if n == 0:
        return 0
    elif n & 1 == 1:
        return f(n - 1) + 1
    elif n & 1 == 0 and n > 0:
        return f(n//2)
count = 0

for i in range(1, 1000000000):
    if f(i) == 2:
        count+= 1
        print(i, count)