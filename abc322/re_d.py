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

def rotate(p):
    return [['#' if p[j][len(p[0])-1-i] == '#' else '.' for j in range(len(p))] for i in range(len(p[0]))]

def fit(grid, poly, x, y):
    for i, row in enumerate(poly):
        for j, cell in enumerate(row):
            if cell == '#' and (x + i >= 4 or y + j >= 4 or grid[x + i][y + j] == '#'):
                return False
    return True

def place(grid, poly, x, y):
    for i, row in enumerate(poly):
        for j, cell in enumerate(row):
            if cell == '#':
                grid[x + i][y + j] = '#'

def solve():
    grid = [['.' for _ in range(4)] for _ in range(4)]
    for poly in polyominoes:
        placed = False
        for x, y in product(range(4), range(4)):
            if any(fit(grid, r, x, y) for r in poly):
                place(grid, next(r for r in poly if fit(grid, r, x, y)), x, y)
                placed = True
                break
        if not placed:
            return "No"
    return "Yes" if all(cell == '#' for row in grid for cell in row) else "No"

polyominoes = []
for _ in range(3):
    poly = [list(input().strip()) for _ in range(4)]
    poly = [[poly[i][j] for j in range(4) if any(poly[x][j] == '#' for x in range(4))] for i in range(4) if any(poly[i][x] == '#' for x in range(4))]
    rotations = [poly]
    for _ in range(3):
        rotations.append(rotate(rotations[-1]))
    polyominoes.append(rotations)

print(solve())
