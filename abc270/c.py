N,X,Y = map(int,input().split())
edge=[[]* N for _ in range(N)]
import sys
sys.setrecursionlimit(int(10 ** 9))
from collections import deque
ans = deque([])
X -= 1
Y -= 1
for i in range(N - 1):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
seen = [False] * N
print(edge)
# xから探索を開始する。
def dfs(x):
    # 今いる場所をansに追加する。
    ans.append(x + 1)

    # 探索済みのindexをTrueにする。
    seen[x] = True


    for nx in edge[x]:
        print(seen,seen[nx],nx,x,ans)
        if nx == Y:
            ans.append(Y + 1)
            print(*ans)
            exit()

        if seen[nx] == False:
            dfs(nx)
            ans.pop()
    
dfs(X)
