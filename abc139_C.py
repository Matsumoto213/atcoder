n = int(input())
h = list(map(int, input().split()))+[float("inf")]
count = 0
ans = 0


for i in range(n - 1):
    if h[i] >= h[i + 1]:
        count += 1
    else:
        ans = max(ans,count)
        count = 0
print(ans)