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


N = II()
# 約数を見つけてリストに格納
divisors = [i for i in range(1, 10) if N % i == 0]

# 結果を格納するリストを準備
result = []

# 0 から N までの各 i について条件を満たす最小の j を見つける
for i in range(N+1):
    for divisor in divisors:
        if i % (N // divisor) == 0:
            result.append(str(divisor))
            break
    else:
        result.append('-')

# 結果を出力
print(''.join(result))