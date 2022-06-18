S,K = input().split()
K = int(K)
import itertools
p = list(itertools.permutations(S))
p = list(set(p))

s = []
for i in range(len(p)):
    s.append("".join(p[i]))
s.sort()
print(s[K - 1])