for i in range(1000, 10_000):
    s = str(i)
    sr = [(int(s[0]) + int(s[1])), (int(s[1]) + int(s[2])), (int(s[2]) + int(s[3]))]
    sr.sort()
    sr.pop(0)
    sr = list(map(str, sr))
    word = ''.join(sr)
    if word == '613':
        print(word, sr, i)
