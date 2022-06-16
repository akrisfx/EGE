
import itertools

coc = 1
for i in itertools.product('абклу', repeat=4):
    print(''.join(i), coc)
    coc += 1