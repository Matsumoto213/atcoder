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

def max_weighted_edges_sum(N, weights):
    # 入力を1次元のリストに変換
    flat_weights = []
    idx = 0
    for i in range(1, N):
        for j in range(N - i):
            flat_weights.append(weights[idx][j])
        idx += 1
    # 重みを降順にソート
    flat_weights.sort(reverse=True)
    # N/2の数だけの辺の重みを合計
    return sum(flat_weights[:N//2])

# 入力
n = int(input())
edge_weights = []
for _ in range(n-1):
    edge_weights.extend(list(map(int, input().split())))

# 出力
print(max_weighted_edges_sum(n, edge_weights))