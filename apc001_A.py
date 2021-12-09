x,y = map(int, input().split())
cnt = 0

if x == y:
    print(-1)
    exit(0)
else:
    while True:
        x *= 2
        
        if x % y != 0:
            print(x)
            exit(0)
        
        cnt += 1
        
        if cnt == 10 ** 6:
            break

print(-1)
