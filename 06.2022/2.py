for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                ok = int( not(x <= y) or (w or not(z)) or w )
                if ok == 0:
                    print(x,y,w,z,'  |', ok)