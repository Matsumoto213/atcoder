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

# グリッドを定義し、関数を呼び出して結果を印刷
grid = []
for _ in range(3):
    L = input().split()
    grid.append(L)
    
def is_disappointing(order):
    # 各列での数字を追跡
    rows = [{}, {}, {}]
    cols = [{}, {}, {}]
    diag1 = {}
    diag2 = {}

    for o in order:
        x, y = o
        val = grid[x][y]

        # 行と列のディクショナリを更新
        rows[x][y] = val
        cols[y][x] = val

        # 対角線のディクショナリを更新
        if x == y:
            diag1[x] = val
        if x + y == 2:
            diag2[x] = val

        # がっかりする条件をチェック
        if len(rows[x]) == 3 and len(set(rows[x].values())) == 2:
            return True
        if len(cols[y]) == 3 and len(set(cols[y].values())) == 2:
            return True
        if len(diag1) == 3 and len(set(diag1.values())) == 2:
            return True
        if len(diag2) == 3 and len(set(diag2.values())) == 2:
            return True

    return False

# 全ての可能な順序を生成
orders = permutations([(x, y) for x in range(3) for y in range(3)], 9)

# がっかりしない順序の数をカウント
not_disappointing_count = sum(1 for order in orders if not is_disappointing(order))

# 全ての可能な順序の数
total_orders = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

# がっかりしない確率を計算
not_disappointing_probability = not_disappointing_count / total_orders

print(not_disappointing_probability)