count = 1
mmx = 0
file = open("./27-A/24.txt").readline()
for i in range(0,len(file)-1):
    if file[i] == file[i+1]:
        count = count + 1
    else:
        if count > mmx:
            mmx = count 
            max_char = file[i]
            ii = i
        count = 1

print(max_char, mmx, ii)