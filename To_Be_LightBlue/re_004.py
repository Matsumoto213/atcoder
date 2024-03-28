N,M = map(int, input().split())
scores = []
for i in range(N):
    score = list(map(int, input().split()))
    scores.append(score)

ans = 0
for i in range(M - 1):
    for j in range(i + 1, M):
        max_ = 0
        for l in range(N):
            max_ += max(scores[l][i],scores[l][j])
        ans = max(max_,ans)
print(ans)