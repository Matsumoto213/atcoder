N,P,Q = map(int, input().split())
D = list(map(int, input().split()))

ans = P
for i in range(N):
    discount = Q + D[i]
    ans = min(ans,discount)
print(ans)