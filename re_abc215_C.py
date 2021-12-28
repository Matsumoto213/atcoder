import itertools
S,K = input().split()
K = int(K)
p = list(itertools.permutations(s))
p = list(set(p))

ans = []
for i in p:
    temp = ''.join(i)
    ans.append(temp)

ans.sort()
print(ans[K - 1])
    