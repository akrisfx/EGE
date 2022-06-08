# for i in range(0, 100):
#     print(i * (99 - i), i , 99 - i)

# print(1 or 0, not(1) or 0, (1) and 0)


# string = str(input())
# print(string[0], string[-1])

from functools import lru_cache

pool = 50

def moves(h, mak = 50):
    arr = [[h*2, mak - h * 2], [h+1, mak - h + 1] , [h+2, mak - h + 2]]
    new = []
    for i in range(len(arr)):
        if arr[i][0] <= mak:
            new.append(arr[i])
    return new

@lru_cache(None)
def f(h):
    if h>= 41 and :
        return 'Srazy'
        
    elif any(f(m)== 'Srazy' for m in moves(h)):
        return 'П1'
    elif all(f(m)== 'П1' for m in moves(h)):
        return 'В1'
    elif any(f(m) == 'В1' for m in moves(h)):
        return 'П2'
    elif all(f(m)=='П1' or f(m)=='П2' for m in moves(h)):
        return 'В2'
    elif any(f(m)=='В1' or f(m)=='В2' for m in moves(h)):
        return 'П3'

for i in range (1,50):
    print(i,  ';', f(i))