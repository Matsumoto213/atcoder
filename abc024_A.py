a,b,c,k = map(int,input().split())
ans = a - b

if k % 2 == 0:
    print(ans)
    exit()
else:
    print(-ans)
    exit()