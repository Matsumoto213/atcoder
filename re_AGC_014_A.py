a,b,c = map(int,input().split())
cnt = 0
 
while True:
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        if cnt == 0:
            print(0)
            break
        
    a /= 2
    b /= 2
    c /= 2
    
    k = a
    a += b
    b += c
    c += k
    
    cnt += 1     
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        print(cnt)
        break
    
    if cnt > 1000:
        print(-1)
        break