N = int(input())
A = list(map(int, input().split()))
from typing import Counter
a = set(A)
a = list(a)
a.sort()
cnt = Counter(A)

ans = [0] * N
for i in range(len(a)):
    ans[len(a) - i - 1] = cnt[a[i]]

for j in range(N):
    print(ans[j])