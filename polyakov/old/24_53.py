file = open("tx\k8data\k8-4.txt").readline()
count = 1
max_ = 0
for i in range(len(file) - 1):
    symbol = file[i]
    if file[i] == file[i + 1]:
        count += 1
    else:
        if count > max_:
            max_ = count
            maxSymbol = file[i - 1]
        count = 1
# print(file)
print(maxSymbol, max_)