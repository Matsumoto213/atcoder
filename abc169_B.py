n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = a[0]
 
for i in range(1,n):
    if ans == 0 or i == 0:
        ans = 0
        break
    else:
        ans *= a[i]
 
if ans > 10 ** 18:
    print(-1)
else:
    print(ans)