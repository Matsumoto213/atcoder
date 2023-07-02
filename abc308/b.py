N,M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))
ans = 0
for i in range(N):
    idx = -1
    if C[i] in D:
        idx = D.index(C[i]) + 1
    
    if idx == -1:
        ans += P[0]
    else:
        ans += P[idx]
print(ans)