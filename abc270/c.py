n,x,y = map(int, input().split())
v = [[] for _ in range(n)]

for i in range(n - 1):
    a,b = map(int, input().split())
    a -= 1 # listのindex参照をそのまま使いたいので頂点id(1から始まっている)を-1しておく
    b -= 1 # aと同様
    v[a].append(b + 1)
    v[b].append(a + 1)
print(v)
# now = x
# while True:
#     print(now)
#     if now == y:
#         break

#     if v[now - 1]