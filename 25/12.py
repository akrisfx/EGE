def f(x):
    d = set()
    count = 0
    for i in range(1,int(x**0.5)+1):
        if  (x % i == 0):
            if ((x//i) % 2==0) and (i%2==0):
                count+=2
            elif (((((x//i) & 1)==0) and ((i&1) != 0)) or ((((x//i) &1)!=0) and ((i&1)==0))):
                count+=1
    if count == 3:
        d|= {i,x//i}
        count = 0
    else:
        count = 0
    return sorted(d)
for u in range(101075762, 102000000):

    if len(f(u))>1:
        print(f(u),u , '----------------')