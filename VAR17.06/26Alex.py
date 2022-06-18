f = open('./f/26-77.txt').readlines()
ar = []
for i in range(len(f)):
    f[i] = f[i][0:-1]
    ar.append(f[i].split(' '))
ar.sort(key=lambda x: x[0])

j = []
cur = 0


for i in range(len(ar)):
    cur = ar[i][0]
