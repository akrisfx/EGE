s = 9**7 + 3**8 - 5

print(s)
new = ''

while s > 0:
    new += str(s%3)
    s = s // 3
print(new)