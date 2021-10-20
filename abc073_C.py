import collections

n = int(input())
lst = [int(input()) for i in range(n)]

lst = collections.Counter(lst)
ans = lst.values()
cnt = 0

for j in ans:
    if j % 2 != 0:
        cnt += 1
print(cnt)
