f = open('./f/17.txt').readlines()
f = [int(x) for x in f]
j = [str(x) for x in f if x % 50 == 0]

allNum = ''.join(j)
sumOfAllC = sum(int(x) for x in allNum)

min_num = 10000000
c = 0

for i in range(len(f) - 1):
    if f[i] > sumOfAllC and f[i + 1] > sumOfAllC:
        c += 1
        min_num = min(min_num, f[i] + f[i + 1])

print(c, min_num)
