import sys
sys.setrecursionlimit(10000)

# 入力の読み込み
N, M = map(int, input().split())
G = [[] for _ in range(N)]

# G[i] は都市iから道路で直接繋がっている都市のリスト
for _ in range(M):
    A, B = map(int, input().split())
    # Pythonではindex0始まりなので、都市iを-1して揃える
    G[A-1].append(B-1)
def dfs(v):
    if seen[v]:
        return
    
    # 初期値でスタートをゴール地として設定 ex)(1, 1)をTrue
    seen[v] = True
    
    for vv in G[v]:
        dfs(vv)

ans = 0

for i in range(N):
    # チェッカー
    seen = [False] * N
    
    # seen[j]は都市jに到達可能かどうかを表す
    dfs(i)
    
    ans += sum(seen)
print(ans)
    
    