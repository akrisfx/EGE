cout = 0

xDefault = 100


for a in range(1, 1000):
    cout = 0
    for x in range(1, 101):
        for y in range(1, 101):
            f = (x // a or (not(x // 6) or not(x // y)))
            if f == False: 
                break
            elif f == True:
                cout += 1

    if (cout == 10000):
        print(a)