H,W = map(int, input().split())
cookies = [input() for _ in range(H)]

def count_remaining_cookies(H, W, cookies):
    marked = [[False] * W for _ in range(H)]
    removed = 0

    def mark_and_remove():
        nonlocal removed
        to_remove = 0

        # Mark rows
        for i in range(H):
            if not any(marked[i]) and len(set(cookies[i])) == 1:
                for j in range(W):
                    marked[i][j] = True
                    to_remove += 1

        # Mark columns
        for j in range(W):
            column = [cookies[i][j] for i in range(H) if not marked[i][j]]

            if len(column) > 1 and len(set(column)) == 1:
                for i in range(H):
                    if not marked[i][j]:
                        marked[i][j] = True
                        to_remove += 1

        removed += to_remove
        return to_remove

    while mark_and_remove() > 0:
        pass

    return H * W - removed

print(count_remaining_cookies(H, W, cookies))
