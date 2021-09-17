n,m,c = map(int, input().split())
b = list(map(int, input().split()))

a = [list(map(int, input().split())) for i in range(n)]

count = 0
for i in range(len(a)):
    ans = 0
    for j in range(len(b)):
        ans += a[i][j] * b[j]
    ans += c
    if ans > 0:
        count += 1
print(count)
