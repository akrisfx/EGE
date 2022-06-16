from functools import lru_cache


def mov(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)

@lru_cache(None)
def f(h):
    if sum(h) >= 77:
        return 'END'
    elif any(f(x) == 'END' for x in mov(h)):
        return 'P1'
    elif all(f(x) == 'P1' for x in mov(h)):
        return 'V1'
    elif any(f(x) == 'V1' for x in mov(h)):
        return 'P2'
    elif all(f(x) == 'P2' or f(x) == 'P1' for x in mov(h)):
        return 'V2'

for i in range(1, 71):
    h = (7, i)
    print(i, f(h))