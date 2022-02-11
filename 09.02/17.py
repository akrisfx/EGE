arr = []
count = 0
for i in range(2476, 7858):
    if i & 1 == 0 and not(i%8 == 0) and int(str(i)[1]) <= 7:
        count += 1
        arr.append(i)
print(count,(max(arr) + min(arr)) / 2)
    