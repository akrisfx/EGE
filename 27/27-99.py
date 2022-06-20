f = open('./f/27_A.txt')
n = int(f.readline())
a = [list(map(int, s.split())) for s in f]
for i in range(len(a)):
    a[i][1] = a[i][1] // 36 + 1
print(a)
minN = 10** 10

for i in range(n):
    sm = 0
    for j in range(n):
        sm += abs(a[i][0] - a[j][0]) * a[j][1]
    if sm < minN:
        minN = sm
        km = a[i][0]
print(minN, km)