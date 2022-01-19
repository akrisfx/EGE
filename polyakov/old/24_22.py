file = open("tx\k7data\k7a-2.txt").readline()
count = 0
max_ = 0
for i in range(0, len(file)):
    if file[i] == "A" or file[i] == "C" or file[i] == "D":
        count += 1
    else:
        if count > max_:
            max_ = count
        count = 0
print(file)
print(max_)

c = ['CCCC', 'CC']
for i in range(len(c)):
    c[i] = c[i][0] + c[i][1:].replace('C', 'c')
print(c)