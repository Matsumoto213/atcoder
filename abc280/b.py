N = int(input())
s = list(map(int, input().split()))

ans = []

for i in range(N):
    if i == 0:
        ans.append(s[i])
    else:
        ans.append(s[i] - s[i - 1])
print(*ans)