import itertools

c = 1
for i, x in enumerate(itertools.product('аеинстфя', repeat=3)):
    word = ''.join(x)
    if word.count('е') == 1:
        if word.count('а') == 0:
            print(c, word, ' ============')
        else:
            print(c, word)
        c += 1


