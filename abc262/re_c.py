N = int(input())
a = list(map(int, input().split()))

for i in range(N):
    a[i] -= 1

x = 0
for i in range(N):
    if a[i] == i:
        x += 1

ans = x * (x - 1) // 2
for i in range(N):
    if a[i] <= i:
        continue

    if a[a[i]] == i:
        ans += 1

print(ans)