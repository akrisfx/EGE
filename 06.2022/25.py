if 126789 % 39 == 0:
    print(126789, 126789 // 39)

# print(10**8)
ar = []

for a1 in range(0, 1000):
    num = int('12' + str(a1) + '6789')
    if num % 39 == 0 and num < 10**8:
        print( num, num // 39 )

arr = [ [500, 'as'], [7, '41d'], [4, 'dswd'], [9, 'awaawdd'],  ]
print(arr)
arr.sort(key= lambda x: x[0])
print(arr)