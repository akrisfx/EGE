cout = 0
for i in range(1, 1000000):
    s = i
    s = 3 * (s // 10)
    n = 1
    while s < 221:
        s = s + 13
        n = n * 2
    if(n == 128):
        cout += 1
        print(i)

print('__________', cout)