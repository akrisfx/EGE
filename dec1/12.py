print('------', '2' in '11111')

a = 4**36 + 3 * 4**20 + 4**15 + 2 * 4**7 + 49
print(a,hex(a))

for i in range(201, 207):
    endStr = '1' * i
    while '111' in endStr or '222' in endStr:
        endStr = endStr.replace('111', '22', 1)
        endStr = endStr.replace('222', '1', 1)

    if ('2' in endStr) == False:
        print(i)