def f(n, b, s):
    for i in range(n):
        s =  [s[0] - 2, s[1] + b]
        s =  [s[0] + 7, s[1] -3]
    return s

ar = [0, 0]
s = [5, -1]

for n in range(-100, 100):
    for b in range(-100, 100):
        if f(n, b, s) == [55, -131]:
            print(n, b)
