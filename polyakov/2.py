for i in range(0,16):
    num = str(bin(i))[2:]
    num =  (4 - len(num)) * '0' + num
    # print(num, bin(i))
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    d = int(num[3])
    res = (not(a) or b) and (not(b == c)) and (not(d) or a)
    if res == True:
        print(a,b,c,d,'  |', res)