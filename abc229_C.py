N,W = map(int, input().split())
L = []

for i in range(N):
    a,b = map(int, input().split())
    L.append([a,b])

L = sorted(L, key=lambda x: x[0],reverse = True)
ans = 0
rem = W

for a,b in L:
    t = min(rem,b)
    ans += t * a
    rem -= t
print(ans)