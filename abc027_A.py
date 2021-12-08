import collections
l1,l2,l3 = map(int, input().split())
L = [l1,l2,l3]
c = collections.Counter(L)

for key,value in c.items():
    if value == 1 or value == 3:
        print(key)
