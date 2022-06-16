from functools import lru_cache


def mov(h):
    a, b = h
    return (a + 3, b), (a * 2, b), (a, b + 3), (a, b * 2)

@lru_cache(None)
def f(h):
    if sum(h) >= 300:
        return 'END'
    elif any(f(x) == 'END' for x in mov(h)):
        return 'P1'
    elif all(f(x) == 'P1' for x in mov(h)):
        return 'V1'
    elif any(f(x) == 'V1' for x in mov(h)):
        return 'P2'
    elif all(f(x) == 'P2' or f(x) == 'P1' for x in mov(h)):
        return 'V2'
    elif any(f(x) == 'V2' or f(x) == 'V1' for x in mov(h)):
        return 'P3'
    elif all(f(x) == 'P3' for x in mov(h)):
        return 'V3'

for i in range(59, 70):
    h = (20, i)
    print(i, f(h))