ans = 0

x = set()
for i in range(1,290001):
    s = str(i)
    for j in range(len(s) - 2):
        if s[j] == s[j + 1] == s[j + 2]:
            if s not in x:
                x.add(s)
                ans += i
print(ans)