# 全てのパターンを試せばいいのでbit全探索を使用する
N,M = map(int, input().split())
A = []
B = []
for i in range(M):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

K = int(input())
C = []
D = []
for i in range(K):
    c,d = map(int, input().split())
    C.append(c)
    D.append(d)

# K人は入力されたc,dどちらかにボールを置く
