n = int(input())
k = int(input())
if k == n:
        print(0)
else:
    vs= n//k
    print(vs*(vs-1)*2)
