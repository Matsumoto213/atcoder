S = input()[::-1]
ans = 0
for i, s in enumerate(S):
    # print(ord(s) -64,s)
    ans += (ord(s) - 64) * 26 ** i
print(ans)