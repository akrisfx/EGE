from functools import lru_cache


def mov(h):
    return h + 1, h * 2

@lru_cache(None)
def f(h):
    if h >= 29:
        return 'END'
    elif any(f(x) == 'END' for x in mov(h)):
        return 'P1'
    elif all(f(x) == 'P1' for x in mov(h)):
        return 'V1'
    elif any(f(x) == 'V1' for x in mov(h)):
        return 'P2'
    elif all(f(x) == 'P2' or f(x) == 'P1' for x in mov(h)):
        return 'V2'

for i in range(1, 30):
    print(i, f(i))