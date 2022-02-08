import collections
N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)
cnt = 0
for a in c:
    if a == c[a]:
        continue
    
    if a > c[a]:
        cnt += c[a]
    else:
        cnt += c[a] - a
print(cnt)