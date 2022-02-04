n,r = map(int, input().split())

import itertools
a = len(list(itertools.combinations(range(n), r)))


print(a)