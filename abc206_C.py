from collections import Counter
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
ans = 0

for i in A:
    ans += N - C[i]
print(ans // 2)