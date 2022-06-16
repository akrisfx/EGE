s = 2197**50 - 169**35 - 26

jeb = 0

while s > 0:
    if s % 13 == 12:
        jeb += 1
    s = s // 13

print(jeb)