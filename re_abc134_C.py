# 二重ループをどう回避するか？
# Numpyで特定のindex以外を抽出する
N = int(input())
A = [int(input()) for _ in range(N)]

for idx,a in enumerate(A):
    idx += 1
    A.pop(idx - 1)
    print(max(A))
    A.insert(idx - 1, a)