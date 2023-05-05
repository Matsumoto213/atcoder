H,W = map(int, input().split())
C = [input() for _ in range(H)]

def count_batsu_marks(C, H, W):
    N = min(H, W)
    S = [0] * (N + 1)

    def check_batsu(i, j, n):
        for d in range(1, n + 1):
            if not (0 < i + d <= H and 0 < j + d <= W and C[i + d - 1][j + d - 1] == '#' and
                    0 < i + d <= H and 0 < j - d <= W and C[i + d - 1][j - d - 1] == '#' and
                    0 < i - d <= H and 0 < j + d <= W and C[i - d - 1][j + d - 1] == '#' and
                    0 < i - d <= H and 0 < j - d <= W and C[i - d - 1][j - d - 1] == '#'):
                return False

        corners = [(i+n+1, j+n+1), (i+n+1, j-n-1), (i-n-1, j+n+1), (i-n-1, j-n-1)]
        if all(0 < x <= H and 0 < y <= W and C[x-1][y-1] == '#' for x, y in corners):
            return False

        return True

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if C[i - 1][j - 1] == '#':
                for n in range(1, N + 1):
                    if check_batsu(i, j, n):
                        S[n] += 1

    return S[1:]

print(*count_batsu_marks(C, H, W))