H,W = map(int, input().split())
A = [input().split() for _ in range(H)]

for L in zip(*A):
    print(*L)