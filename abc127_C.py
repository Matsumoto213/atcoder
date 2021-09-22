import collections
 
n,m = map(int, input().split())
lst = []
 
for i in range(m):
    l,r = map(int, input().split())
    for j in range(l,r + 1):
        lst.append(j)
 
count = collections.Counter(lst)
ans = count.values()
ans = list(ans)
print(ans.count(m))