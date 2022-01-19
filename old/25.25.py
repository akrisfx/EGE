import math
for i in range(1000000, 2000000):
    cout = 0
    for k in range(math.floor(math.sqrt(i)) - 50, math.ceil(math.sqrt(i))):
        if (i % k) == 0 and (abs(k - (i // k)) <= 100):
            cout+=1
    if cout >=3:
        print(i)