

import itertools


s = '1' * 10 + '2' * 3
ss = 'aabc'

arr = list(itertools.permutations(s, len(s))) 

print(arr)