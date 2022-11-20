h,m = map(int, input().split())

while True:
    # 0うめ
    hh = str(h).zfill(2)
    mm = str(m).zfill(2)
    if 0 <= int(hh[0] + mm[0]) < 24 and 0 <= int(hh[1] + mm[1]) < 60:
        print(h,m)
        exit()
    
    m += 1

    if m >= 60:
        h += 1
        m %= 60
    
    if h >= 24:
        h %= 24