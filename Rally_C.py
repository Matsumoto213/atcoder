N = int(input())
X = list(map(int, input().split()))

ans = 10 ** 15
for i in range(1,101):
    temp = 0
    for j in range(N):
        temp += (X[j] - (i + 1)) ** 2
    ans = min(temp, ans)
print(ans)