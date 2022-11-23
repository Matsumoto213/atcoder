h,m = map(int, input().split())

while True:
    H = str(h).zfill(2)
    M = str(m).zfill(2)
    if int(H[0] + M[0]) < 24 and int(H[1] + M[1]) < 60:
        print(h,m)
        exit()
    
    m += 1
    if m >= 60:
        m %= 60
        h += 1
    
    if h >= 24:
        h %= 24