
from functools import lru_cache


def mov(h):
    a, b = h
    return  (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)
def f(h):
    if sum(h) >= 247:
        return 'END'
    elif any(f(x) == 'END' for x in mov(h)):
        return 'П1'
    elif all(f(x) == 'П1' for x in mov(h)):
        return 'В1'
    elif any(f(x) == 'В1' for x in mov(h)):
        return 'П2'
    elif all(f(x) == 'П2' or f(x) == 'П1' for x in mov(h)):
        return 'В2'

for i in range(50, 200):
    h = 17, i
    print(i, f(h))