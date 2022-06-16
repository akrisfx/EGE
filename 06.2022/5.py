arr = []
for i in range(1, 1000):
    b = str(bin(i))[2:]
    if i & 1 == 0:
        b = '10' + b + '10'
    elif i & 1 == 1:
        b = '1' + b + '00'
    b = int(b, 2)
    if b > 100:
        arr.append(b)

print(min(arr))
