# 動的計画法でとくが、いまいち理解することができていない
s = input()
mod = (10 ** 9) + 7
lenS = len(s)
t = 'chokudai'
dp = [0] * (len(t) + 1)
dp[0] = 1

for i in range(lenS):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[j + 1] += dp[j]
print(d[8] % mod)