N = int(input())
W = list(map(int, input().split()))

ans = 10 ** 18 + 8
for i in range(N):
    right,left = sum(W[:i + 1]),sum(W[i + 1:])
    tmp = abs(right - left)
    if tmp < ans:
        ans = min(abs(right - left),ans)
print(ans)