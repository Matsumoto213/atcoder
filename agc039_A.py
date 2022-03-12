S = input()
K = int(input())
ans = 0

# 連続する文字列の個数を数える
i = 1
series = 1
while True:
    if i > len(S) - 1:
        break

    if S[i - 1] == S[i]:
        series += 1
    else:
        ans += series // 2
        series = 1
    
    if i == len(S) - 1 and series > 1:
        ans += series // 2

    i += 1
print(ans * K)