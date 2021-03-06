
from functools import lru_cache


def mov(h):
    return  h + 1, h * 2 # ретерним список возможных ходов (из условия задачи)
                         # тут по условию задачи мы можем добавить + 2 в одну кучу или увеличить вдвое * 2
@lru_cache(None) # это нужно чтобы было неограниченное кэширование 
def f(h):
    if h > 53: # исходя из условия задачи, кто-то выигрывает если в куче 243 или больше камней
        return 'END' # при этом мы не рассматриваем те i при которых f(i) == 'END' ткк игра по факту закончилась без ходов кого-то из челиксов
    elif any(f(x) == 'END' for x in mov(h)):  # тут, побеждает первым ходом петя(П1), если любой( `any` ) из его возможных ходов ( `for x in mov(h)` заканчивает 'END')
        return 'П1'
    elif all(f(x) == 'П1' for x in mov(h)):   # здесь, мы ставим ( all ) если ваня побеждает при ЛЮБОМ ходе пети
        return 'В1'                           # иначе, если ваня побеждает после НЕУДАЧНОГО хода пети то ставим ( any )
    elif any(f(x) == 'В1' for x in mov(h)):   # тут также по логике
        return 'П2'
    elif all(f(x) == 'П2' or f(x) == 'П1' for x in mov(h)): # тут если в условии сказано или после первого хода или после второго, и первый не гарантирован
        return 'В2'

for i in range(1, 55):
    print(i, f(i))

