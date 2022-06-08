
import itertools
col = 0
sog = ['аа', 'бб', 'вв', 'гг', 'дд']

for i in itertools.product('абвгд', repeat=5):
    word = ''.join(i)
    ok = 1
    for x in sog:
        ok *= int((word[0] != 'а') and (x not in word))
    if ok:
        print(word)
        col += 1

print(col)

# 1024
