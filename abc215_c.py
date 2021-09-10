import itertools
s,k  = map(str, input().split())
k = int(k)


p = list(itertools.permutations(s))
p = list(set(p))

ans = []

for i in p:
    str = ''.join(i)
    ans.append(str)

ans.sort()
print(ans[k - 1])
