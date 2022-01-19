s = 'ВУАЛЬ'
arr = []
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            for l in range(len(s)):
                for m in range(len(s)):
                    st = (f'{s[i]}{s[j]}{s[k]}{s[l]}{s[m]}')
                    if st[0] != 'Ь' and st.count('А') == 1 and st.count('В') == 1 and st.count('У') == 1 and st.count('Л') == 1 and st.count('Ь') == 1 and not st in arr:
                        arr.append(st)
                        print(st)
                        
print(len(arr))

count = 0

for i in range(len(arr)):
    for j in range(len(arr[i]) - 1):
        if arr[i][j] == 'Ь' and arr[i][j + 1] == 'У' or arr[i][j + 1] == 'А':
            count += 1
            break
    
print(len(arr) - count)  
