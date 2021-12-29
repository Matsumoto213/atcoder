from collections import defaultdict
from collections import defaultdict
# defaultdictを使えば、簡単に辞書を作ることができる
N, K = map(int, input().split())
dct = defaultdict(int)
L = []
for i in range(N):
  A, B = map(int, input().split())
  dct[A] += B
L = list(dct.keys())
L.sort()

now = 0
walk = 0

for i in L:
    if i <= now + K:
        K = now + K - i + dct[i]
        walk += i - now
        now = i
    else:
        walk += K
        K = 0
        
if K != 0:
    walk += K
        
print(walk)