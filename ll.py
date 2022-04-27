
s = 1
i = 10

while s < 100000000000000000:
    s *= 2

koef = 1
print(s)
new = 1
n = float('0.'+ '0' * 30 + '1')

startNum = s
while s > n:
    # if str(i)[-1] == '0' and str(i)[-2] == '0':
    koef = new / startNum 
    print(s, koef)
    i += 1
    
    s = s / 2
    new = new + s
    

