s = input()
x = [s[i] for i in range(len(s))]
n = len(x)

ans = (n - 1) * 2

for i in range(1, n - 1):
    if x[i] == 'U':
        temp = (n - i - 1) + (i * 2)
        ans += temp
    else:
        temp = i + ((n - i - 1) * 2)
        ans += temp
print(ans)