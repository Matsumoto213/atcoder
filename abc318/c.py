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

N,D,P = MI()
F = LI()

def min_travel_cost(N, D, P, fares):
    # 運賃を昇順にソート
    fares.sort(reverse=True)

    total_cost = 0
    i = 0
    while i < N:
        # D日分の通常運賃の合計を計算
        sum_fare = sum(fares[i:i+D])

        # D日分の通常運賃の合計がP円よりも高い場合、周遊パスを使用
        if sum_fare > P:
            total_cost += P
            i += D
        else:
            total_cost += fares[i]
            i += 1

    return total_cost

print(min_travel_cost(N,D,P,F))