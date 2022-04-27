import math

print(5 & 1)

min_num = 50002
count_num = 0

for i in range(10001, 50001):
    count = 1
    for k in range(1, i//2 +3):
        if i % k == 0:
            count += 1
            if count > 17:
                count_num += 1
                if i < min_num:
                    min_num = i
                break

print(count_num, min_num)