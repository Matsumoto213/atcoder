import sys
input = sys.stdin.readline
from collections import *
 
N, P = map(int, input().split())
A = list(map(int, input().split()))
dp = [[0]*2 for _ in range(N+1)]
dp[0][0] = 1
 
for i in range(N):
    for j in range(2):
        dp[i+1][j] += dp[i][j]
        dp[i+1][(j+A[i])%2] += dp[i][j]
    print(dp)
 
print(dp[N][P])