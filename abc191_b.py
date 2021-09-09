n,x = map(int, input().split())
lst =list(map(int, input().split()))
ans = []

for i in lst:
    if i != x:
        ans.append(i)
print(*ans)
