import math
N,K = map(int, input().split())
A = list(map(int, input().split()))

if N == K:
    print(1)
    exit(0)

temp = N - K
n = math.ceil(temp / (K - 1))
print(n + 1)
