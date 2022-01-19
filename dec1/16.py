cout = 0
def f(n):
    if n == 0:
        return 0
    elif n > 0 and n & 1 == 0:
        return f(n//2)
    elif n & 1 == 1:
        return 1 + f(n-1)


for i in range(1, 501):
    if f(i) == 8:
        cout += 1

print(cout)