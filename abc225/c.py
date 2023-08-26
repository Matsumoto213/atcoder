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
A = LLI(N)

if N == 1:
    for j in range(M - 1):
        right = A[0][j + 1]
        if A[0][j] + 1 != right:
            print('No')
            exit()
elif M == 1:
    for j in range(N - 1):
        bottom = A[j + 1][0]
        if A[j][0] + 7 != bottom:
            print('No')
            exit()
else:
    seven = False
    after_seven = 0
    for i in range(N - 1):
        for j in range(M - 1):
            if A[i][j] % 7 == 0:
                seven = True
            if seven:
                after_seven += 1
            right = A[i][j + 1]
            bottom = A[i + 1][j]
            if A[i][j] + 1 != right or A[i][j] + 7 != bottom or seven and after_seven:
                print('No')
                exit()
print('Yes')