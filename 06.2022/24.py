f = open('D:/Programming/EGE/06.2022/f/24.txt').readline()
i = 0
cur = 0
ar = [0 for i in range(26)]
# print(ar)
# print(ord('Z'), ord('A') - 65)

# for i in f:
#     ar[ord(i) - 65] += 1

# for i in range(len(ar)):
#     print(chr(i + 65), ar[i])






f = f.replace('A', ' ')
f = f.split(' ')
for i in range(0, len(f)):
    if len(f[i]) > 7:
        d = f[i]
        print(d)
# print(f)
        

# # print(len('BBDDBBDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBBBBBBBBBBDDDDDDDDBBBBDDDDBB'))

# while i < len(f) - 1:
#     word = f[i] + f[i + 1]
#     if word == 'BB' or word == 'DD':
#         cur += 1
#         i += 2
#     else:
#         if cur > 3:
#             ar.append(cur)
#             print(i)
#         cur = 0
#         i += 1

print((ar))
# print(f[3172662 - 700: 3172662 + 1000])