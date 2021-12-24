# 解けたが計算量の問題
from collections import Counter
N = int(input())
A = list(map(int, input().split()))

def Sum(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

for i in range(N):
    L = A[:i] + A[i + 1:]
    C = Counter(L)
    values, counts = zip(*C.most_common())
    ans = 0
    counts = list(counts)
    for j in counts:
        n = Sum(j - 1)
        ans += n
    print(ans)
    