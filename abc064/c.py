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

N  = II()
A = LI()
color = {'灰':0,'茶':0,'緑':0,'水':0,'青':0,'黄':0,'橙':0,'赤':0}

other = 0
for i in range(N):
    if A[i] >= 1 and A[i] <= 399:
        color['灰'] += 1
    elif A[i] < 800:
        color['茶'] += 1
    elif A[i] < 1200:
        color['緑'] += 1
    elif A[i] < 1600:
        color['水'] += 1
    elif A[i] < 2000:
        color['青'] += 1
    elif A[i] < 2400:
        color['黄'] += 1
    elif A[i] < 2800:
        color['橙'] += 1
    elif A[i] < 3200:
        color['赤'] += 1
    else:
        other += 1
mi = 0
for key,value in color.items():
    if value > 0:
        mi += 1

if mi == 0 and other > 0:
    print(1, other)
else:
    print(mi, mi + other)