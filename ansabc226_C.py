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
