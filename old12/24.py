
file = open('//old12/files/24.txt').readlines()
coun = 0


for i in range(len(file)):
    if file[i].count('J') > file.count('E'):
        coun += 1

print(coun)