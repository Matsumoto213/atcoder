H,W = map(int,input().split())

min_ = 10 ** 18 + 17
A = []
for i in range(H):
    a = list(map(int, input().split()))
    min_a = min(a)
    min_ = min(min_a,min_)
    A.append(a)

ans = 0

for i in range(H):
    for j in range(W):
        ans += A[i][j] - min_
print(ans)