after = 33333334
c = 0
for i in range(200_000_000, 400_000_001):
    for m in range(2, int(i ** 0.5)+ 2, 2):
        if (i // 6 * m) & 1 == 1:
            print(i)

print(c)

# for i in range(399_999_001, 400_000_001):
#     if i % 6 == 0:
#         print(i)

print((399999996 - 200_000_004) // 12 + 1)


