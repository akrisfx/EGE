import itertools
from timeit import repeat


# for i in itertools.product('01', repeat=3):
#     print(''.join(i))
# Виктор составляет 4-буквенные коды из букв В, И, К, Т, О, Р. Каждую букву можно использовать не более одного
#  раза, при этом нельзя ставить рядом две гласные и две согласные. Сколько различных кодов может составить
#  Виктор?

sog = []
for i in itertools.product('вктр', repeat=2):
    sog.append(''.join(i))
print(sog)

gl = ['ио','ои']
    

col = 0

for i in itertools.permutations('виктор', 4):
    # print(''.join(i))
    word = ''.join(i)
    ok = 1
    for x in sog:
        if x in word: 
            ok = 0

    for y in gl:
        if y in word:
            ok = 0
    if ok == 0:
        continue

    col += 1
    print(word)
print(col)

