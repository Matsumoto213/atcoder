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
from itertools import accumulate
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

N,Q = MI()
S = I()

L = [0] * (N + 1)
for i in range(N - 1):
    if S[i] == S[i + 1]:
        L[i + 1] = 1

L = list(accumulate(L))
for _ in range(Q):
    l, r = MI()
    l -= 1
    r -= 1
    print(L[r] - L[l])