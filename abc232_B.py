import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LISI(): return list(map(int, SI()))
def LA(f): return list(map(f, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return input().strip('\n')
def MS(): return input().split()
def LS(): return list(input().strip('\n'))
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def gen_matrix(h, w, init): return [[init] * w for _ in range(h)]
INF = float('inf')
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from math import ceil, floor, log2, log, sqrt, gcd
from itertools import combinations as comb, combinations_with_replacement as comb_w, product, permutations
from collections import deque, defaultdict
from pprint import pprint
# import numpy as np    # cumsum
from functools import reduce, lru_cache     # decorator: メモ化. max_size=128
import operator


def gen_array(tpl: tuple, init):
    res = f'[{init}]*{tpl[-1]}'
    for t in reversed(tpl[:-1]):
        res = f'[{res} for _ in range({t})]'
    return eval(res)

alphabet={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,
"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

def solve():
    S = SI()
    T = SI()
    
    ans = set()
    
    for i in range(len(S)):
        K = (ord(T[i]) - ord(S[i]) + 26) % 26
        ans.add(K)
    
    print('Yes' if len(ans) == 1 else 'No')
    
if __name__ == '__main__':
    solve()