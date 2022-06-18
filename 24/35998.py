f = open('./files/35998.txt').readlines()
f = [x[:-1] for x in f]

max_cur = -1000

for i in f:
    if i.count('A') < 25:
        for j in range(65, 91): # 1е решение через split()
            spl = i.split(chr(j))
            leng = len(i) - len(spl[0]) - len(spl[-1]) - 1
            max_cur = max(max_cur, leng)

        # for j in range(65, 91): # 2е решение лобовое
        #     leng = (len(i) - i[::-1].index(chr(j)) - 1) - i.index(chr(j))
        #     if leng > max_cur:
        #         max_cur = leng
        #         print(leng, i, chr(j), len(i) - 1 -i[::-1].index(chr(j)), i.index(chr(j)))

print(max_cur)
print(chr(90))

