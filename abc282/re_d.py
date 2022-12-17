
from collections import deque
from collections import defaultdict

MAX_V = 1000
N,M = list(map(int,input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    s, t = map(int,input().split())
    G[s - 1].append(t)
    G[t - 1].append(s)

color = [0] * MAX_V
def dfs(v, c):
    '''
    深さ優先探索を利用して、ノードvに色c(1 or -1)を塗っていく関数。
    隣接ノードと異なる色が塗れなくなったらFalseを返す。
    '''
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    return True

L = []

for i in range(N):
    L.append(i)

ans = 0
import itertools
for key,value in itertools.combinations(L, 2):
    if value not in G[key] and key not in G[value]:
        G[key].append(value)
        G[value].append(key)
        if dfs(key,value) == False:
            ans += 1
print(ans)