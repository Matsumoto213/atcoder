import collections
N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)
c = dict(c)
ans = 0

for idx,i in enumerate(A):
    idx = N - (idx + 1)
    ans += idx + c[i] - 1
    c[i] -= 1
print(ans)
    