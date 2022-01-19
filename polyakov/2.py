for i in range(0, 16):
    num = bin(i)[2:]
    num =  (4 - len(num)) * '0' + num
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    d = int(num[3])
    vir = (not((not(b)) or a)) and (not(c) or d) != (a and b and c and (not(d)))
    if vir == True:
        print(a,b,c,d,'  |', vir)