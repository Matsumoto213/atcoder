INF = float('inf')
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from math import ceil, floor, log2, log, sqrt, gcd
from itertools import combinations as comb, combinations_with_replacement as comb_w, product, permutations
from collections import deque, defaultdict
from pprint import pprint
import numpy as np
from functools import reduce, lru_cache     # decorator: メモ化. max_size=128
import operator
def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LISI(): return list(map(int, SI()))
def LA(f): return list(map(f, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def I(): return input()
def SI(): return input().strip('\n')
def MS(): return input().split()
def LS(): return list(input().strip('\n'))
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def gen_matrix(h, w, init): return [[init] * w for _ in range(h)]
d = [(1, 0),(1, 1),(0, 1),(-1, 1),(-1, 0),(-1, -1),(0, -1),(1, -1)]
H,W = MI()
S = LLS(H)
seen = [[False] * W for _ in range(H)]
for i in range(H) :
    for j in range(W) :
        if S[i][j] != "#" :
            seen[i][j] = True
def dfs(x,y):
    seen[x][y] = "."
    for dr, dc in d:
        nr = x + dr
        nc = y + dc

        if (0 <= nr < H) and (0 <= nc < W):
            if seen[nr][nc]:
                continue
            dfs(nr,nc)

ans = 0
for i in range(H):
    for j in range(W):
        if not seen[i][j]:
            dfs(i,j)
            ans += 1
print(ans)