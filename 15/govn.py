p = [2,4,6,8,10,12,14,16,18,20]
q = [5,10,15,20,25,30,35,40,45,50]
q = [x for x in range(5, 51, 5)]
print(q)

for i, x in enumerate(p):
    print(i, x)

for i in p:
    print(i)

for i in range(len(p)):
    x = p[i]
    print(i, x)