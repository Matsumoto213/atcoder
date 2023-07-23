N = int(input())
H = list(map(int, input().split()))
ans = 1
max_ = H[0]
for i in range(1,N):
    if H[i] >= max_:
        ans += 1
        max_ = H[i]
print(ans)