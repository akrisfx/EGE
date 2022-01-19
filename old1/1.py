for i in range(0, 16):
    num = bin(i)[2:]
    num =  (4 - len(num)) * '0' + num
    x = int(num[0])
    y = int(num[1])
    z = int(num[2])
    w = int(num[3])
    vir = ((not(x) or y) == (not(z) or w)) or (x and w)
    if vir == False:
        print(x,y,z,w,'  |', vir)

# Ответ: ZYXW