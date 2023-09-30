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

from itertools import product

def rotate(polyomino):
    return [''.join(polyomino[j][3 - i] for j in range(4)) for i in range(4)]

def possible_placements(polyomino):
    placements = set()
    for _ in range(4):  # 回転
        for i, j in product(range(5), repeat=2):  # グリッド内での可能な位置全てを試す
            placement = [['.' for _ in range(4)] for _ in range(4)]
            fit = True
            for x, y in product(range(4), repeat=2):
                if polyomino[x][y] == '#':
                    nx, ny = x + i, y + j
                    if nx >= 4 or ny >= 4:
                        fit = False
                        break
                    if placement[nx][ny] == '#':
                        fit = False
                        break
                    placement[nx][ny] = '#'
            if fit:
                placements.add(tuple(''.join(row) for row in placement))
        polyomino = rotate(polyomino)
    return placements

def solve(polyominos):
    for placement1 in possible_placements(polyominos[0]):
        for placement2 in possible_placements(polyominos[1]):
            for placement3 in possible_placements(polyominos[2]):
                grid = [['.' for _ in range(4)] for _ in range(4)]
                for i, j in product(range(4), repeat=2):
                    count = sum([placement1[i][j] == '#', placement2[i][j] == '#', placement3[i][j] == '#'])
                    if count > 1:
                        break
                    if count == 1:
                        grid[i][j] = '#'
                else:
                    if all(grid[i][j] == '#' for i, j in product(range(4), repeat=2)):
                        return True
    return False

# 入力を受け取る
polyominos = []
for _ in range(3):
    polyomino = [input().strip() for _ in range(4)]
    polyominos.append(polyomino)

# 解く
if solve(polyominos):
    print('Yes')
else:
    print('No')

