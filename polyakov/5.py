# for i in range(1,36):
#     r = bin(i)[2:]
#     if i & 1 == 0:
#         r = r + '01'
#     else:
#         r = r + '10'
#     intr = int(r, 2)
#     if intr > 138:
#         print(i, intr)

for i in range(1, 1000000):
    s = i
    n = 12
    while s > 0:
        s = s - 10
        n = n + 7
    if n == 61:
        print(i)