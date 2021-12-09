s = input()
t = input()
ans = -10 ** 8

for i in range(len(s) - len(t) + 1):
    ma = 0
    string = s[i:i + len(t)]
    for j in range(len(t)):
        if string[j] == t[j]:
            ma += 1
        ans = max(ma,ans)
print(len(t) - ans)