from typing import Counter

n = int(input())
a = list(map(int, input().split(' ')))
 
counter = Counter(a)
s = sorted(set(a))
 
l = len(s)
ans = [0] * n
for i in range(l):
    ans[l - i - 1] = counter[s[i]]
    print(ans)
# print(ans)