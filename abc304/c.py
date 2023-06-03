import math
from collections import deque

def solve(N, D, points):
    # 全ノード間の距離を計算し、D以内にあるノード間を接続
    edges = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            dist = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            if dist <= D:
                edges[i].append(j)
                edges[j].append(i)

    # BFSで感染可能なノードを探索
    infected = [0]*N
    infected[0] = 1
    q = deque([0])
    while q:
        node = q.popleft()
        for neighbor in edges[node]:
            if infected[neighbor] == 0:
                infected[neighbor] = 1
                q.append(neighbor)
    
    return infected

N, D = map(int, input().split())
points = [list(map(int, input().split())) + [i] for i in range(N)]

ans = solve(N, D, points)

for i in ans:
    if i:
        print('Yes')
    else:
        print('No')