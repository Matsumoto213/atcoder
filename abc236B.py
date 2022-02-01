n = int(input())
N = list(map(int, input().split()))

from collections import Counter

c = Counter(N)
temp = (n * 4) / n

for key,val in c.items():
    if val != temp:
        print(key)
        exit(0)
    