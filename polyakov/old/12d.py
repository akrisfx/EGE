s = 'КАПКАН'
arr = []
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            for l in range(len(s)):
                for m in range(len(s)):
                    for n in range(len(s)):
                        st = (f'{s[i]}{s[j]}{s[k]}{s[l]}{s[m]}{s[n]}')
                        if st.count('А') == 2 and st.count('К') == 2 and st.count('П') == 1 and st.count('Н') == 1 and not st in arr:
                            arr.append(st)
                            print(st)
                        
print(len(arr))

count = 0

for i in range(len(arr)):
    for j in range(len(arr[i]) - 1):
        if arr[i][j] == arr[i][j + 1]:
            count += 1
            break
    

print(len(arr), len(arr) - count)

        
    