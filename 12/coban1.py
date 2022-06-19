s = '25' * 13 + '5'

while '25' in s:
    s = s.replace('25', '9', 1)
    print(s, flush=False)

print(s, sum(int(c) for c in s))
