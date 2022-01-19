m1 = [2,4,6,8,10,12]
m2 = [4,8,12,116]
m3 = m1
m4 = [0,1,3,5,7,9]


for a in range(1, 150):
    cout = 0
    for x in range(1, 1000):
        if not(x in m1) or (not((x in m2) and not(x in m4)) or not(x in m3)):
            cout += 1
        else:
            break
    
    print(a, cout)