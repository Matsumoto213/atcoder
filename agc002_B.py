N,M = map(int, input().split())
judge = [False] * N
num = [1] * N
temp = 1
for i in range(M):
    x,y = map(int, input().split())
    num[x - 1] -= 1
    num[y - 1] += 1

    if temp == x:
        judge[y - 1] = True
        temp = y

ans = 0
for i in range(N):
    if judge[i] and num[i] > 0:
        ans += 1

print(ans)
