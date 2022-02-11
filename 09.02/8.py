import itertools

count = 0

arr = list(itertools.product(['1','2','3'], repeat=6))
for i in range(len(arr)):
    word = ''.join(arr[i])
    if word.count('3') == 2:
        count += 1
        print(word)
print(count)