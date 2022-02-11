for i in range(100, 1000):
    istr = str(i)
    f_i = str(int(istr[0]) + int(istr[1]))
    s_i = str(int(istr[1]) + int(istr[2]))
    if int(f_i) > int(s_i):
        if f_i + s_i == '1712':
            print(i)
    else:
        if s_i + f_i == '1712':
            print(i)