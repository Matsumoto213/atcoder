import numpy as np
N,K = map(int, input().split())
A = list(map(int, input().split()))
xy = [list(map(int,input().split())) for _ in range(N)]

# 一番遠い箇所のマンハッタン距離を求める。
