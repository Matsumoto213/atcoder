N = int(input())
s = input()
lenS = len(s)
ans = -10 ** 8

for i in range(lenS):
    x = s[:i + 1]
    y = s[i + 1:]
    same_n = len(set(x) & set(y))
    ans = max(same_n,ans)
print(ans)