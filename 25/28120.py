def f(x):
    d = set()
    for i in range(1, int(x**0.5) + 2):
        if x % i == 0:
            d.add(i)
            d.add(x // i) 
            if len(d) > 4:
                return []
    return sorted(d)

for i in range(201455, 201471):
    ok = f(i)
    if len(ok) == 4:
        print(ok)