
import itertools


# ss = list(itertools.product('николай', repeat=11))

# print(ss[:15])
count = 0

for i in itertools.product('николай', repeat=11):
    if i[0] != 'й' and i.count('и') == 1 and i.count('о') == 1 and i.count('а') == 1:
        count += 1
        if count % 10000 == 0:
            print(''.join(i), count)
print(count)