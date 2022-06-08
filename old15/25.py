
from math import sqrt


def m(k):
    return 950000000 + k

def searc(num): # нахождение количества четных делителей
    count = 0
    for i in range(2, num // 2 + 2, 2):
        if num % i == 0:
            count += 1
    return count + 1

print((sqrt(5)) % 1)

# for i in range(2, 1000, 2):
#     cock = searc(i)
#     if cock & 1 == 1:
#         print(i, searc(i))
# for i in range ( 950000000, 950000000 + 5000000):
#     if i % 18 == 0 and i % 32 == 0 and i % 50 == 0 and i % 98 == 0 and i % 72 == 0 and i % 128 == 0 and i % 200 == 0 and i % 162 == 0 and i % 242 == 0 and i % 288 == 0:
#         print(i)
ss = 950118976
print(sqrt(ss))
print(searc(ss))

for i in range(28, 1000, 2):
    cur = m(i)
    # print(i, ' -----------')
    # if searc(cur) & 1 == 1:
    #     print(i)
    if sqrt(cur) % 1 == 0 :
        print(cur, '-----')
