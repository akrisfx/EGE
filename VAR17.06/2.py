for x in range(0, 2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                ok = ((x and y) <= (not z or w)) and ((w or x) or (not y))
                if not ok:
                    print(x,w,y,z, '   |', ok)
#                 #  ((x and y) <= (not z or w)) and ((w or z) or (not y))
print('((x and y) <= (not z or w)) and ((w or z) or (not y))' == '((x and y) <= (not z or w)) and ((w or x) or (not y))')

