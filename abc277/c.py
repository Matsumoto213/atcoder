N = int(input())
from collections import defaultdict
from collections import deque
ab = defaultdict(list)

# from functools import lru_cache
# @lru_cache
# def dfs(T,i):
#     Q = deque([i])
#     q = Q.popleft()
#     for c in T[q]:
#         print(c)
#         dfs(T,c)

for i in range(N):
    a, b = map(int, input().split())
    ab[a].append(b)
    ab[b].append(a)

ans = -10 ** 18
# for i in range(len(ab[1])):

