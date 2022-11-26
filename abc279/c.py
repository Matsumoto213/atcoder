import sys
input = sys.stdin.readline
from collections import defaultdict
H,W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]
s = defaultdict(list)
# Sを並び替えてTにできるかどうか
for j, chars in enumerate(zip(*S)):
    chars = list(chars)
    chars = ''.join(chars)
    if chars not in s:
        s[chars] = 1
    else:
        s[chars] += 1

t = defaultdict(list)
for j, chars in enumerate(zip(*T)):
    chars = list(chars)
    chars = ''.join(chars)
    if chars not in t:
        t[chars] = 1
    else:
        t[chars] += 1

for key,value in s.items():
    if key not in t or t[key] != value:
        print('No')
        exit()

print('Yes')