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

N = II()
votes = [LI() for _ in range(N)]

def min_votes(N, regions):
    # 各選挙区の鞍替えが必要な票数を計算
    diffs = []
    total_seats = sum(z for _, _, z in regions)
    needed_seats = total_seats // 2 + 1
    takahashi_seats = 0

    for x, y, z in regions:
        # 現在の高橋君の票数
        takahashi_votes = x

        # 青木君が多数派の場合
        if x <= y:
            diff = y - x + 1
            for i in range(1, z + 1):
                diffs.append((diff, i))
                diff += 2

        # 高橋君が多数派の場合
        else:
            takahashi_seats += z

    diffs.sort()

    # 必要な鞍替え票数をカウント
    total_votes = 0
    for diff, seats in diffs:
        if takahashi_seats >= needed_seats:
            break
        total_votes += diff
        takahashi_seats += seats

    return total_votes

print(min_votes(N, votes))