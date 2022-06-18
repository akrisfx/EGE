f = open('./files/37131.txt').readline()
f = f.replace('KL', ' ')
f = f.replace('LK', ' ')
f = f.split(' ')
l = [len(x) for x in f]
lol = max(l)
print(lol + 2, f[l.index(lol)])

print('AACVFLKawdsaLK'.split('LK'))