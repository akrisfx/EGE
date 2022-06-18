f = open('./files/36037.txt').readline().split('XZZY')
f = [len(x) for x in f]
print(max(f) + 6)
print([x for x in range(1, 10)])
