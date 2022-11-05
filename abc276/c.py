N = int(input())
p = list(map(int,input().split()))
l = []
import itertools
for i in range(1,N + 1):
    l.append(i)

from operator import itemgetter
def permutation(order):
    print(order)
    return itemgetter(*order)
print(permutation(l))