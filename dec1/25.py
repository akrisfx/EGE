def findD(num):
    cout = 0
    um = 1
    for i in range(2, num // 2 + 2):
        if cout == 5:
            break
        if (num % i == 0):
            um = um * i
            cout += 1
    return [um, cout]

for i in range(200000000, 300000000):
    finded = findD(i)
    print(i)
    if finded[1] > 4 and finded[0] < i:
        print('-----------', i, '-----------')


