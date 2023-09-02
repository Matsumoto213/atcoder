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
rect = LLI(N)
def calc_area(N, rects):
    # 最大値を見つけるための初期設定
    max_x, max_y = 0, 0
    for rect in rects:
        max_x = max(max_x, rect[1])  # Bi
        max_y = max(max_y, rect[3])  # Di

    # カバーされているかをカウントする2次元配列
    covered = [[0 for _ in range(max_y+1)] for _ in range(max_x+1)]

    for rect in rects:
        for x in range(rect[0], rect[1]):  # Ai to Bi-1
            for y in range(rect[2], rect[3]):  # Ci to Di-1
                covered[x][y] += 1

    # 1回以上カバーされているセルの数をカウントする
    area = sum(1 for row in covered for cell in row if cell > 0)

    return area

print(calc_area(N, rect))