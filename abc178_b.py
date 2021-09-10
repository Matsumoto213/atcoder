a,b,c,d = map(int, input().split())
ans = -10 ** 8
for i in range(a , b + 1):
    for j in range(c, d + 1):
        ans1 = i * j
        ans = max(ans,ans1) 
print(ans)


