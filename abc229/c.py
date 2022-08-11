N,W = map(int, input().split())
L = []

# Wグラム以下でチーズの美味しさを最大化する。
for _ in range(N):
    a,b = map(int, input().split())
    L.append([a,b])

l = sorted(L, key=lambda x: x[0],reverse = True)

ans = 0
gram = 0
temp = W
for a,b in l:
    tem = min(temp,b)
    temp -= tem
    ans += tem * a
    if temp == 0:
        break
print(ans)