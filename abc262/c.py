N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    for j in range(i + 1,N):
        if i + 1 == a[j] and j + 1 == a[i] or i + 1 == a[i] and j + 1 == a[j]:
            ans += 1
print(ans)