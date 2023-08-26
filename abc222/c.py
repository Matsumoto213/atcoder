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
hand = LLS(N * 2)

def judgeWinner(a,b):
    judge = ''
    if a == 'P':
        if b == 'P':
            judge = 'Draw'
        elif b == 'C':
            judge = 'Lose'
        elif b == 'G':
            judge = 'Win'
    elif a == 'C':
        if b == 'P':
            judge = 'Win'
        elif b == 'C':
            judge = 'Draw'
        elif b == 'G':
            judge = 'Lose'
    elif a == 'G':
        if b == 'P':
            judge = 'Lose'
        elif b == 'C':
            judge = 'Win'
        elif b == 'G':
            judge = 'Draw'
    return judge

# 勝敗を管理する
situation = defaultdict(list)
for i in range(1,N * 2 + 1):
    situation[i] = 0

for j in range(M):
    for i in range(0,N * 2,2):
        # sitution[i]とsituation[i + 1]の人がじゃんけんをする
        player1 = hand[list(situation.keys())[i] - 1][j]
        player2 = hand[list(situation.keys())[i + 1] - 1][j]

        judge = judgeWinner(player1, player2)
        if judge == 'Win':
            situation[list(situation.keys())[i]] += 1
        elif judge == 'Lose':
            situation[list(situation.keys())[i + 1]] += 1
        else:
            continue

    sorted_items = sorted(situation.items(), key=lambda kv: (-kv[1], kv[0]))
    # 既存のdefaultdictの内容を上書き
    situation.clear()
    situation.update(sorted_items)

for key in situation.keys():
    print(key)