S,K = input().split()
K = int(K)

import itertools
l = list(set(itertools.permutations(S,len(S))))
l.sort()
print("".join(list(l[K - 1])))
    