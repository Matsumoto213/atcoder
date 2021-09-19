# bit全探索
from itertools import product

N = 3

for p in product((0, 1), repeat=N):
    print(p)