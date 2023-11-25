INF = float('inf')
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from math import ceil, floor, log2, log, sqrt, gcd
from itertools import combinations as comb, combinations_with_replacement as comb_w, product, permutations
from collections import deque, defaultdict, Counter
from pprint import pprint
import numpy as np
from functools import reduce, lru_cache     # decorator: メモ化. max_size=128
import operator
import re
from scipy.special import comb as cmb

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

def calculate_mex(arr):
    n = len(arr)
    count = [0] * (n + 1)
    for num in arr:
        if num < n:
            count[num] += 1

    for i in range(n + 1):
        if count[i] == 0:
            return i

def process_queries(N, A, queries):
    mex = calculate_mex(A)
    count = [0] * (N + 1)
    for num in A:
        if num < N:
            count[num] += 1

    results = []
    for i, x in queries:
        if A[i-1] < N:
            count[A[i-1]] -= 1
            if count[A[i-1]] == 0 and A[i-1] < mex:
                mex = A[i-1]

        A[i-1] = x
        if x < N:
            count[x] += 1
            if count[x] == 1 and x == mex:
                while mex < N and count[mex] > 0:
                    mex += 1

        results.append(mex)

    return results

N,Q = MI()
A = LI()
queries = []
for i in range(Q):
    i,x = MI()
    queries.append((i,x))

ans = process_queries(N, A, queries)

for i in range(len(ans)):
    print(ans[i])
