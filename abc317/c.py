def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LISI(): return list(map(int, SI()))
def LA(f): return list(map(f, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return input().strip('\n')
def MS(): return input().split()
def LS(): return list(input().strip('\n'))
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def gen_matrix(h, w, init): return [[init] * w for _ in range(h)]
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

N,M = MI()
edges = [LI() for _ in range(M)]

# グラフを作成
graph = [[] for _ in range(N)]
for a, b, c in edges:
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

max_distance = 0

def dfs(node, visited, distance):
    global max_distance
    visited[node] = True
    local_max = distance
    for next_node, next_distance in graph[node]:
        if not visited[next_node]:
            local_max = max(local_max, dfs(next_node, visited[:], distance + next_distance))
    max_distance = max(max_distance, local_max)
    return local_max

for start_node in range(N):
    dfs(start_node, [False] * N, 0)

print(max_distance)