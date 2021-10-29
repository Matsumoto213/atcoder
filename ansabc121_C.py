n,m = map(int,input().split())
ba=[()]*n
for i in range(n):
    a,b= map(int,input().split())
    ba[i] = a,b
ba.sort(key = lambda x:x[0])
i=0
ans=0
while m:
    a,b = ba[i]
    if m>=b:
       ans += a*b
       m -= b
    else:
        ans += a*m
        m=0
    i+=1
print(ans)        