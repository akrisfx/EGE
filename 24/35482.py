f = open('./files/35482.txt').readlines()
# print(f[1:3])
f = [i[:-1] for i in f]
# print(f[1:3])
maxx = 1111111
for i in f:
    coc = i.count('G')
    if coc < maxx:
        maxx = coc
        cur = i

# print(cur, maxx)
for i in range(65, 93):
    print(cur.count(chr(i)), chr(i))