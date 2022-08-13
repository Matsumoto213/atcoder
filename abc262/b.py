n, m = map(int, input().split())
graph = [[] for _ in range(n)]
l = [i for i in range(1,n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す
import itertools
p = list(itertools.combinations(l,3))
ans = 0
for a, b, c in itertools.combinations(range(n), 3):
    if a in graph[b] and b in graph[c] and c in graph[a]:
        ans += 1
print(ans)