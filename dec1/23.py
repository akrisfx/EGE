f = open("dec1/files/24.txt").readline()

arr= []
freeA = True
cout = 0
maxCout = 0
curCh = f[0]

for i in range(1,len(f)):
    if f[i] == curCh:
        cout += 1
    elif f[i] == 'A' and freeA:
        freeA = False
        cout += 1
    else:
        if(cout > maxCout):
            maxCout = cout
        cout = 0
        freeA = True
        curCh = f[i]
print(maxCout)




