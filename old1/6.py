for a in range(1, 100):
    cout = 0
    for x in range(1, 101):
        for y in range(1, 101):
            if (y + 2*x != 99) or (y>a) or (x>a):
                cout += 1
            else:
                break
    
    print(a, cout)