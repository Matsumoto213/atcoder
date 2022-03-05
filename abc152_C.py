N = int(input())
P = list(map(int, input().split()))
ans = 1
min_ = P[0]
# 1回のみのループで条件を満たせ

for i in range(1, N):
    if P[i] < min_:
        ans += 1
    min_ = min(P[i],min_)
print(ans)
