import collections
N = int(input())
S = [int(input()) for _ in range(N)]

c = collections.Counter(S)
ans = c.value()
print(ans[0])