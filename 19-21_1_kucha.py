
from functools import lru_cache


def mov(h):
    return  h + 2, h * 2

@lru_cache(None)
def f(h):
    if h > 242:
        return 'END'
    elif any(f(x) == 'END' for x in mov(h)):
        return 'П1'
    elif all(f(x) == 'П1' for x in mov(h)):
        return 'В1'
    elif any(f(x) == 'В1' for x in mov(h)):
        return 'П2'
    elif all(f(x) == 'П2' or f(x) == 'П1' for x in mov(h)):
        return 'В2'

for i in range(1, 242):
    print(i, f(i))
