s = input()

if 'a' not in s:
    print(-1)
    exit()
else:
    ans = 0
    for i in range(len(s)):
        if s[i] == 'a':
            ans = i + 1
print(ans)