b16 = 'A'
s = '0123456789ABCDEF'
for i in range(0, 8):
    print(int('1' + str(i) + '3', 8))

for i in range(len(s)):
    print(int('A' + s[i], 16))
