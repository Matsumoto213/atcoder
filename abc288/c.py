from typing import List
N,M = map(int, input().split())
a = []
b = []
for i in range(M):
    u,v = map(int, input().split())
    a.append(u)
    b.append(v)

class UnionFind:
    def __init__(self, n):
        self.p = [-1 for _ in range(n)]

    def find(self, x):
        if self.p[x] < 0:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.p[x] < self.p[y]:
            self.p[x] += self.p[y]
            self.p[y] = x
        else:
            self.p[y] += self.p[x]
            self.p[x] = y

def minimum_removed_edges(n: int, m: int, a: List[int], b: List[int]) -> int:
    uf = UnionFind(n)
    edges = [(a[i]-1, b[i]-1) for i in range(m)]
    edges.sort(key=lambda x: x[0])

    cnt = 0
    for edge in edges:
        x, y = edge
        if uf.find(x) != uf.find(y):
            uf.union(x, y)
            cnt += 1
    return m - cnt

print(minimum_removed_edges(N,M,a,b))