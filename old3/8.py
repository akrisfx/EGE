import itertools

count = 0

arr = list(itertools.product(['А','Н','Д','Р','Е','Й'], repeat=6))
for i in range(len(arr)):
    word = ''.join(arr[i])
    if word.count('А') > 1 and word.count('Й') < 2:
        count += 1
print(count)