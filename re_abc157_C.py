N,M = map(int, input().split())
dct = {}

for i in range(1,N + 1):
    dct[i] = 10

for i in range(1,M + 1):
    s,c = map(int, input().split())
    if dct[s] > c:
        dct[s] = c

val = list(dct.values())
for i in range(N):
    if val[i] == 10:
        val[i] = str(0)
    else:
        val[i] = str(val[i])

ans = ''.join(val)

if ans[0] == '0':
    print(-1)
else:
    print(ans)
