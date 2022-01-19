for a in range(1, 100):
    cout = 0
    for x in range(1, 10000):
        if not(x & 33 == 0) or (not(x & 45 != 0) or x & a != 0):
            cout += 1
        else:
            break
    if cout == 9999:
        print(a, cout)
