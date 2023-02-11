N = int(input())
ans = 10 ** 18 + 7
for i in range(N):
    a,p,x = map(int,input().split())
    temp = 10 ** 18 + 7
    if x - a > 0:
        temp = p
    ans = min(ans,temp)

if ans == 10 ** 18 + 7:
    print(-1)
else:
    print(ans)