# どこに駒を置くのか
N,M = map(int, input().split())
x = list(map(int, input().split()))

x.sort()

l = []

# それぞれの差分を求める
for i in range(M - 1):
    l.append(abs(x[i + 1] - x[i]))
l.sort()

ans = 0
for i in range(M - N):
    ans += l[i]

print(ans)