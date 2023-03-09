n = int(input())
a = list(map(int, input().split()))

count = [0] * 200
for i in range(n):
    r = a[i] % 200
    count[r] += 1
ans = 0
for i in range(200):
    k = count[i]
    if k >= 2:
        ans += (k * (k - 1)) // 2

print(ans)