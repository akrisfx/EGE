s = 343**5 + 343**4 + 49**6 - 7**13 - 21

new = ''
while s > 0:
    new += str(s % 7)
    s = s // 7
new = new[::-1]
print(new)
