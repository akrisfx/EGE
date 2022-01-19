for a in range(1, 100000):
    cout = 0
    for x in range(1, 10000):
        if (x % a == 0 or not(x%6 == 0) or not(x % 9 == 0)):
            cout += 1
        else:
            break
    if cout == 9999:
        print(a, cout)