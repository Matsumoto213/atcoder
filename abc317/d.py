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

def minimum_votes_to_win(N, votes):
    # 各選挙区での必要な鞍替え票数を計算
    need_votes = []
    total_seats = 0
    takahashi_seats = 0

    for i in range(N):
        X, Y, Z = votes[i]
        total_seats += Z
        if X > (X + Y) // 2:  # すでに高橋君が多数派
            takahashi_seats += Z
        else:
            # 必要な鞍替え票数を計算
            required = (X + Y) // 2 + 1 - X
            need_votes.append((required, Z))

    # 必要な鞍替え票数の「コストパフォーマンス」でソート
    need_votes.sort(key=lambda x: x[0]/x[1])

    print(need_votes)
    ans = 0
    for required, Z in need_votes:
        if takahashi_seats > total_seats // 2:
            break
        ans += required
        takahashi_seats += Z

    return ans
print(minimum_votes_to_win(N, votes))
