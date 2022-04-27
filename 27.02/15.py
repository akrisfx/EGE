def d(n, m):
    if n % m == 0:
        return True
    else:
        return False

count = 0
colX = 10000

for a in range(1, 10000000):
    count = 0
    for x in range(1, colX):

        if d(144, a) and ((not( not(d(x, a)) and d(x, 66) ) or (not(d(x, 105))))):
            count += 1
    if count == colX - 1:
        print(a, count)
