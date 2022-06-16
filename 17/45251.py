f = open('./17/f/45251.txt').readlines()
f = list(map(int, f))

mi = 168
c = 0
mox = 0

# for i in f:
#     if i % 21 == 0:
#         mi = min(mi, i)

# print(mi)

for i in range(len(f) - 1):
    if f[i] % mi == 0 or f[i+ 1] % mi == 0:
        c += 1
        mox = max(mox, f[i] + f[i + 1])

print(c, mox)