
f = open('//27.02/27/17-3.txt').readlines()
col_pair = 0
min_raz = 1000000

for i in range(len(f) - 2):
    f[i] =  float(str(f[i])[:-1])
    f[i+1] =  float(str(f[i+1])[:-1])
    f[i+2] =  float(str(f[i+2])[:-1])
    ar = [f[i], f[i+1], f[i+2]]
    if ar[0] < ar[1] and ar[1] < ar[2]:
        col_pair += 1
        razn = max(ar) - min(ar)
        if razn < min_raz:
            min_raz = razn

print(col_pair, min_raz)

