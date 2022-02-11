new = ''
s = 4**14 + 64**16 - 18
while s > 0:
    new = new + str(s%4)
    s = s//4
print(s, new[::-1])
print(new.count('0'))


