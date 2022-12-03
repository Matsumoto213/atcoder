N,X = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
judge = [False] * N
idx = X - 1
while True:
    if judge[idx]:
        break
    judge[idx] = True
    ans += 1
    idx = a[idx] - 1
print(ans)