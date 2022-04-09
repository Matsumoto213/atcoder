x = int(input())
dp = [0] * (x + 1)
dp[0] = 1

for i in range(x):
    if dp[i] == 0:
        continue

    for j in range(100,106):
        if i + j <= x:
            dp[i + j] = 1
    print(dp,i)

print(1 if dp[x] else 0)