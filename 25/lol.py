def f(x):
    d = set()
    for i in range(1, int(x**0.5) + 2):
        if x % i == 0:
            if i & 1 == 1:
                d.add(i)
            jj = x // i
            if jj & 1 == 1:
                d.add(jj)
        if len(d) > 7:
            return [0]
    return sorted(d)

for i in range(95632, 95651):
    gg = list(f(i))
    # print(gg, i)
    if len(gg) == 6:
        print(gg)
    
        
