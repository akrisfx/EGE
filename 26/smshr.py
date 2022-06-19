
f = open('./f/smashr.txt').readlines()
f.pop(0)
f = [int(x) for x in f]

sor = sorted(f)
half = sor[2499]
quart = sor[3750]
c = 0
minn = 100000000

print(sor[3749])
for i in range(len(f)-1):
    for j in range(i + 1, len(f)):
        sus = f[i] + f[j]
        if sus & 1 == 0:
            avg = sus // 2
            if (half < avg) and (quart > avg):
                c += 1
                minn = min(avg, minn)

print(c, minn)  # 2405042 546772
# print(sor[3749])

