H,W,X,Y = map(int, input().split())
S = [input() for _ in range(H)]
X -= 1
Y -= 1

ans = 1
# 横
for j, chars in enumerate(zip(*S)):
    if j == Y:
        h = [chars[i] for i in range(H)]


for i, char in enumerate(S):
    if i == X:
        w = [char[k] for k in range(W)]

# 縦
for i in range(X - 1, -1, -1):
    if h[i] == '#':
        break
    else:
        ans += 1

for i in range(X + 1, H):
    if h[i] == '#':
        break
    else:
        ans += 1
# 横
for i in range(Y - 1, -1, -1):
    if w[i] == '#':
        break
    else:
        ans += 1
for i in range(Y + 1, W):
    if w[i] == '#':
        break
    else:
        ans += 1

print(ans)