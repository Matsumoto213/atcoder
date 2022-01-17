# 辞書の重複あり
N,M = map(int, input().split())
from collections import defaultdict

a = []
b = []
ab = defaultdict(list)

for i in range(M):
    A,B = map(int, input().split())
    ab[A].append(B)

temp = ab[1]
judge = False

for i in temp:
    key = ab[i]
    if N in key:
        judge = True
    
print('POSSIBLE' if judge else 'IMPOSSIBLE')
