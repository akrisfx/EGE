f = open('./06.2022/f/17.txt').readlines()

f = list(map(int, f))
ar = []


maxx = 89958

for i in range(0, len(f) - 1):
    if f[i] > maxx or f[i + 1] > maxx:
        ar.append(f[i] + f[i + 1])

print(len(ar), min(ar))