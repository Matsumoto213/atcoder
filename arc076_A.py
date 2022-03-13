mod = 10 ** 9 + 7
N,M = map(int, input().split())
import math

if N == M:
    ans = 2 * (math.factorial(N) * math.factorial(M))

if abs(N - M) == 1:
    ans = math.factorial(N) * math.factorial(M)

if abs(N - M) > 1:
    ans = 0

print(ans % mod)