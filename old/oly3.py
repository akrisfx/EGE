s=int(input())
e=int(input())
n=int(input())
arrPortals=[]
absol=1000000000
secAbsol=1000000000

for i in range(0, n):
    arrPortals.append(int(input()))

for i in range(0,n):
    if (abs(arrPortals[i] - s)) < absol:
        absol = abs(arrPortals[i] - s)

for i in range(0, n):
    if (abs(arrPortals[i] - e)) < secAbsol:
        secAbsol = abs(arrPortals[i] - e)

if abs(s - e) < (absol + secAbsol + 1):
    print(abs(s - e))
else:
    print(absol + secAbsol + 1)