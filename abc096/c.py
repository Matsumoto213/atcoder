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
import re
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

H,W = MI()
S = LLS(H)

# S(i,j)が'#'の場合、上下左右のどれかが'#'でなければならない

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            if i == 0:
                if j == 0:
                    if S[i + 1][j] != '#' and S[i][j + 1] != '#':
                        print('No')
                        exit()
                elif j == W - 1:
                    if S[i + 1][j] != '#' and S[i][j - 1] != '#':
                        print('No')
                        exit()
                else:
                    if S[i + 1][j] != '#' and S[i][j + 1] != '#' and S[i][j - 1] != '#':
                        print('No')
                        exit()
            
            elif i == H - 1:
                if j == 0:
                    if S[i - 1][j] != '#' and S[i][j + 1] != '#':
                        print('No')
                        exit()

                elif j == W - 1:
                    if S[i - 1][j] != '#' and S[i][j - 1] != '#':
                        print('No')

                else:
                    if S[i - 1][j] != '#' and S[i][j + 1] != '#' and S[i][j - 1] != '#':
                        print('No')
                        exit()
            else:
                if j == 0:
                    if S[i + 1][j] != '#' and S[i - 1][j] != '#' and S[i][j + 1] != '#':
                        print('No')
                        exit()

                elif j == W - 1:
                    if S[i + 1][j] != '#' and S[i - 1][j] != '#' and S[i][j - 1] != '#':
                        print('No')
                        exit()
                else:
                    if S[i + 1][j] != '#' and S[i - 1][j] != '#' and S[i][j - 1] != '#' and S[i][j + 1] != '#':
                        print('No')
                        exit()
print('Yes')