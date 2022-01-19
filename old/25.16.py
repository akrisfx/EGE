a = 1000000
cout = 0
arr = []

for a in range(1062100, 2000000):
    if cout >= 6:
        arr.append(a)
        print(a)
    cout = 0
    for i in range(800, a //800 + 1 ):
        for j in range(i - 101, i + 101):
            if (max(i, j) - min(i, j) < 101 and i * j == a):
                cout += 1
                print(a, max(i, j), min(i, j))
                break 

print(arr)

