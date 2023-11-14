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
d = [(1, 0),(1, 1),(0, 1),(-1, 1),(-1, 0),(-1, -1),(0, -1),(1, -1)]
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

A = [list(map(int, input().split())) for _ in range(9)]
N = 9

# それぞれi = 0, j = 0の時に行と列を見る

# それぞれ9マスを確認するときは以下のパターン
# (0,0),(0,3),(0,6)
# (3,0),(3,3),(3,6)
# (6,0),(6,3),(6,6)

# つまり i % 3 == 0 and j % 3 == 0 の時に確認する
for i in range(N):
    for j in range(N):
        L = set()

        if i % 3 == 0 and j % 3 == 0:
            L.add(A[i][j])
            L.add(A[i + 1][j])
            L.add(A[i + 2][j])
            L.add(A[i][j + 1])
            L.add(A[i][j + 2])
            L.add(A[i + 1][j + 1])
            L.add(A[i + 1][j + 2])
            L.add(A[i + 2][j + 1])
            L.add(A[i + 2][j + 2])
            if len(L) != 9:
                print('No')
                exit()
        
        if i == 0:
            L = set([row[j] for row in A])
            if len(L) != 9:
                print('No')
                exit()

        if j == 0:
            L = set(A[i])
            if len(L) != 9:
                print('No')
                exit()

print('Yes')