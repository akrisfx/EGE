
s = '9' * 292

while '222' in s or '9999' in s:
    if '222' in s:
        s = s.replace('222', '9', 1)
    elif '9999' in s:
        s = s.replace('9999', '2', 1)
    print(s)
print(s)