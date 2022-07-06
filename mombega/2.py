import itertools


for x in range (2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                ok = not(x <= z) or (y == w) or not y
                if not ok:
                    print(x, z, y, w, '   |', int(ok))

for i in itertools.product('01', repeat=4):
    # print(''.join(i))
    x = int(i[0])
    y = int(i[1])
    w = int(i[3])
    z = int(i[2])
    ok = not(x <= z) or (y == w) or not y
    if not ok:
        print(x, z, y, w, '   |', int(ok))