
def automatron(num):
    binStr = str(bin(num))[2:-1]
    if num & 1 == 1:
        binStr += '10'
    else:
        binStr += '01'
    intFinal = int(binStr, 2)
    
    return intFinal
    

for i in range(1, 1000000):
    output = automatron(i)
    if output == 2018:
        print(i)
