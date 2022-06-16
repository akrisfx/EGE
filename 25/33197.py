

for i in range(1000000, 2000001):
    arr = set()
    for j in range(1,  int((i**0.5) + 3)):
        # print("A")
        ost = i % j
        second = i // j
        razn = abs(second - j)
        # print(ost, second, razn)
        if ost == 0 and razn <= 100:
            arr.add(razn)
            if len(arr) >= 3:
                print(i, sorted(arr))
                break

