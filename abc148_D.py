n = int(input())
a = list(map(int, input().split()))

cnt = 0

for i in range(n):
    if a[i] == cnt + 1:
        print(a[i],i)
        cnt += 1

if cnt == 0:
    print(-1)
else:
    print(n - cnt)