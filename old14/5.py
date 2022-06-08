
for i in range(1, 10000):
    s = bin(i)[2:]
    # print(type(s))
    if i & 1 == 0:
        s = s + '10'
    else:
        s = '1' + s + '10'
    if int(s, 2) > 516:
        print(i)
        break