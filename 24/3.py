lol = list(range(0, 9 + 1))
arr = []

for i in range(len(lol)):
    lol[i] = str(lol[i])


file = open('./24/files/24_3.txt').readline()
cur = ''
for i in file:
        if i in lol:
            cur += i
        else:
            if cur != '':
                new = int(cur)
                if new & 1 == 0:
                    arr.append(new)
                cur = ''

print(arr)