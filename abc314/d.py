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
S = LS()
Q = II()
x = [0] * Q
c = [''] * Q
upperFlg = None
# 1の場合はそれぞれそのまま文字を変更する
# 2及び3の場合はその都度全ての文字を変更していると処理に間に合わないため工夫する
# 最後に出たのが小文字か大文字かを判断して処理が終わった後に大文字・小文字の変換を行う。
# しかし、その都度変更したものと見られるため、値は保持する必要がある

change = []
for i in range(Q):
    t,x[i],c[i] = MS()
    x[i] = int(x[i])
    if t == '1':
        S[x[i] - 1] = c[i]
        change.append([x[i] - 1,c[i]])
    elif t == '2':
        upperFlg = False
        change = []
    elif t == '3':
        upperFlg = True
        change = []

if upperFlg is not None:
    if upperFlg:
        S = [char.upper() for char in S]
    else:
        S = [char.lower() for char in S]

for i in range(len(change)):
    index = change[i][0]
    change_letter = change[i][1]
    S[index] = change_letter

print(''.join(S))