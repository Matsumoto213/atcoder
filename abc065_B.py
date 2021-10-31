N = int(input())
A = [int(input()) for _ in range(N)]

now = 1
cnt = 0

for i in range(N + 1):
    if now == 2:
        print(cnt)
        exit()
    now = A[now - 1]
    cnt += 1
print(-1)