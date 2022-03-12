v,a,b,c = map(int, input().split())

i = 0
while True:
    if i == 3:
        i = 0
    
    if i == 0:
        v -= a
        if v < 0:
            print('F')
            exit()
    elif i == 1:
        v -= b
        if v < 0:
            print('M')
            exit()

    elif i == 2:
        v -= c
        if v < 0:
            print('T')
            exit()
    i += 1
