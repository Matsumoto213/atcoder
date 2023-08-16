N,M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)

def dfs(v,seen):
    seen[v] = True
    for vv in G[v]:
        if seen[vv]:
            continue
        dfs(vv,seen)

ans = -1
for v in range(N):
    seen = [False] * N
    dfs(v, seen)

    ok = True

    for i in range(N):
        if(seen[i] == False):
            ok = False
    if(ok):
        ans = v + 1
print(ans)