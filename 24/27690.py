f = open('./files/27690.txt').readline()


cc = 1
maxx = 0
for i in range(len(f) - 1):
    if f[i] != f[i + 1]:
        cc += 1
    else:
        maxx = max(maxx, cc)
        cc = 1
maxx = max(maxx, cc)
print(maxx)