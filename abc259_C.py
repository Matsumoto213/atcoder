S = input()
T = input()

from collections import defaultdict
# defaultdictを使えば、簡単に辞書を作ることができる
dct = defaultdict(int)
d = defaultdict(int)

for i in range(len(S)):
    dct[S[i]] += 1

for i in range(len(T)):
    d[T[i]] += 1


for key,value in d.items():
    if value < dct[key] or value >= 2 and dct[key] < 2:
        print('No')
        exit()

print('Yes')