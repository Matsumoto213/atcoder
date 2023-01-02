S = input()
ans = 0
len = len(S)

if len % 2 != 0:
    right = S[:len // 2]
    left = S[len // 2 + 1:]
else:
    right = S[:len // 2]
    left = S[len // 2:]

left = left[::-1]
ans = 0
for i in range(len // 2):
    if right[i] != left[i]:
        ans += 1
print(ans)