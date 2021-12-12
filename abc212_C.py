# 計算量を減らす方法
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

L = []

for a in A:
    n = bisect_left(B,a)
    if n == 0:
        L.append(abs(B[n] - a))
    elif i == len(B):
        L.append(abs(B[n - 1] - a))
    else:
        L.append(min(abs(B[n - 1] - a), abs(B[n] - a)))
print(min(L))
        