arr = []
count = 0
for i in range(3614033, 3614116):
    for j in range(3, i // 2 + 2, 2):
        if i % j == 0:
            count += 1
            break        
    if count == 0:
        arr.append(i)
    count = 0
for i in range(len(arr)):
    print(i + 1, arr[i])
        