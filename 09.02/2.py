for i in range(0,16):
    num = str(bin(i))[2:]
    num =  (4 - len(num)) * '0' + num
    # print(num, bin(i))
    w = int(num[0])
    z = int(num[1])
    y = int(num[2])
    x = int(num[3])
    res = (not(x) or not(y)) and (not(x == z)) and w
    if res == True:
        print(x,w,z,y,'  |', res)