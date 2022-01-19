# from itertools import combinations_with_replacement
#
import itertools

s = 'ПСКАЛЬ'
#
#
# def check(word):
#     words = ''.join(word)
#     if words[0] != 'Ь' and not ('ЬЬ' in words) and len(words) == 4:
#         return words
#
#
# arr, arr2 = list(map(check, combinations_with_replacement(s, 4))), []
# print(len(arr))
#
# for i in range(len(arr)):
#     if arr[i] is not None:
#         arr2.append(arr[i])
# print(len(arr2), arr2)

count = 0  # method 1
for w1 in s: 
    for w2 in s:
        for w3 in s:
            for w4 in s:
                word = w1+w2+w3+w4
                if word[0] != 'Ь' and not ('ЬЬ' in word):
                    count += 1
                    print(word)
print(count)

count2 = 0  # method 2 with func
arr3 = list(itertools.product(['П', 'С', 'К', 'А', 'Л', 'Ь'], repeat=4)) 
for i in range(len(arr3)):
    worded = ''.join(arr3[i])
    if worded[0] != 'Ь' and not ('ЬЬ' in worded):
        count2 += 1
print(count2)
