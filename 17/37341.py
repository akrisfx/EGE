f = open('./17/f/37341.txt').readlines()
f = list(map(int, f))

c = 0
ar = 0

for i in range(0, len(f) - 1):
    for j in range(i + 1, len(f)):
        if abs(f[i] - f[j]) & 1 == 0 and (f[i] % 19 == 0 or f[j] % 19 == 0):
            c += 1
            ar = max(ar, f[i] + f[j])

print(c, ar)

