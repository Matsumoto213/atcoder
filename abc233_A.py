x,y = map(int, input().split())

cnt = 0
if x >= y:
    print(0)
else:
    while True:
        if x >= y:
            print(cnt)
            break
        
        x += 10
        cnt += 1
