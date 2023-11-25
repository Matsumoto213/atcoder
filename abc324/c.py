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

# Tが一部変更されてしまっている可能性あり

N,T = MS()
N = int(N)

# 文字数が同じ場合
def judge1(A, B):
    dif_cnt = 0
    for a,b in zip(A,B):
        if a != b:
            dif_cnt += 1
    return dif_cnt

# 文字列が違う場合
def judge2(A,B):
    # 短い方をA,長い方をBで固定
    if len(A) > len(B):
        A,B = B,A
    j = 0
    # 長い方の文字列からある文字を削除して短い方の文字列になる」かどうかで判定
    for i in range(len(A)):
        if A[i] == B[j]:
            j += 1
            continue
        j += 1
        if i + 1 != j:
            return False
        if A[i] == B[j]:
            j += 1
        else:
            return False
    return True

ans = []
for i in range(1, N + 1):
    S = input()
    if len(S) == len(T):
        if judge1(S, T): ans.append(i)
    elif abs(len(S) - len(T)) == 1:
        if judge2(S, T): ans.append(i)

print(len(ans))
print(*ans)