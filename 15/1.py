def d (n, m):
    return n % m == 0

def foo (x, A):
    return (not d(x, A)) <=(d(x, 6) <= (not d(x, 9)))

for a in range(1, 10000):
    ok = True
    for x in range(1, 1000):
        if not(foo(x,a)):
            ok = False
            break
    if ok == True:
        print(a)