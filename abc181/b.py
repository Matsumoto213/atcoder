N = int(input())
ans = 0
for i in range(N):
    a,b = map(int, input().split())
    temp = ((a + b) / 2) * (b - a + 1)
    ans += temp
print(int(ans))