N = int(input())
X = list(map(int, input().split()))

ans = 10 ** 10
for i in range(min(X), max(X) + 1):
    print(i)
    total = 0
    for j in range(N):
        total += (i - X[j]) ** 2
    ans = min(ans,total)
print(ans)