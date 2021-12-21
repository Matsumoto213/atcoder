from collections import Counter

N = int(input())
A = list(map(int, input().split()))

A.sort()
L = Counter(A)
key = L.keys()
key = list(key)

ma = -10 ** 8

if N == 1:
  print(1)
  exit(0)

for idx,i in enumerate(key):
    # 左端の場合
    if idx == 0:
        diff = abs(key[idx + 1] - i)
        if diff <= 1:
            cnt = L[i] + L[i + 1]
        else:
            cnt = L[i]

    # 右端の場合
    elif idx == len(key) - 1:
        diff = abs(key[idx - 1] - i)
        if diff <= 1:
            cnt = L[i] + L[i - 1]
        else:
            cnt = L[i]
        
        
    # 真ん中の場合
    else:
        diff_ma_1 = abs(key[idx - 1] - i)
        diff_pl_1 = abs(key[idx + 1] - i)
        
        if diff_ma_1 <= 1 and diff_pl_1 <= 1:
            cnt = L[i] + L[i - 1] + L[i + 1]
        elif diff_ma_1 <= 1 and diff_pl_1 > 1:
            cnt = L[i] + L[i - 1]
        elif diff_pl_1 <= 1 and diff_ma_1 > 1:
            cnt = L[i] + L[i + 1]
        else:
            cnt = L[i]
    ma = max(ma,cnt)
print(ma)