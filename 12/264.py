for i in range(1, 30):
    for j in range(1, 30):
        for k in range(1, 30):
            s = '0' + '1'*i + '2'*j + '3'*k
            jj = s
            while ('01' in jj) or ('02' in jj) or ('03' in jj):
                jj = jj.replace('01', '2302', 1)
                jj = jj.replace('02', '10', 1)
                jj = jj.replace('03', '201', 1)
            if jj.count('1') == 51 and jj.count('2') == 29 and jj.count('3') == 23:
                print(s, jj, k)
