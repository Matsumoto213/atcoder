# 二重ループをどう回避するか？
# Numpyで特定のindex以外を抽出する
# お見事！このような数学が苦手な人にも理解できて簡単なコードこそ至高
N = int(input())
A = [int(input()) for _ in range(N)]
B = sorted(A, reverse = True)

for a in A:
    if a == B[0]:
        print(B[1])
    else:
        print(B[0])