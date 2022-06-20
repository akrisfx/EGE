def f(n, base):
    new = ''
    s = n
    while s > 0:
        new += str(s % base)
        s = s // base
    return new[::-1]


nn = []
for i in range(1, 9, 2):
    nn.append(str(i) + '0')
    nn.append('0' + str(i))
    for j in range(1, 9, 2):
        nn.append(str(i) + '0' + str(j))

print(nn)
cc = 0
for i in range(10000, 100000):
    new = f(i, 9)
    if new.count('0') == 1:
        if not any(new.count(x) == 1 for x in nn):
            print(new)
            cc += 1

print(cc)

# print(f(10, 9))
