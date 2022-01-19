count = 0
arr = []
buffer = []
for i in range(190201, 190281):
    for j in range(2, i + 1, 2):
        if i % j == 0:
            count += 1
            buffer.insert(0, j)
            if count > 4:
                count = 0
                buffer = []
                break
    if count == 4:
        arr.append(buffer)
        buffer = []
        count = 0
# print(arr)
for i in range(len(arr)):
    print(arr[i])        

    