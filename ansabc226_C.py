def solve():
    # スタックを使ったDFSです（dequeを使ってBFSにしてもいいです）
    seen = [False] * (N + 1)
    stack = [N]
    seen[N] = True

    ans = 0

    while stack:
        u = stack.pop()
        ans += T[u]

        for v in G[u]:
            if not seen[v]:
                seen[V] = True
                stack.append(v)
    return ans


N = int(input())
T = [0] * (N + 1)
G = [[] for _ in range(N + 1)]

for u in range(1, N + 1):
    T[u], k, *A = map(int, input().split())
    for v in A:
        G[u].append(v)
        G[v].append(u)
print(solve())