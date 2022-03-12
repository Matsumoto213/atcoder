N = int(input())
S = input()
from collections import Counter
len_S = len(S)

c = Counter(S)
left_W = 0

ans = 10 ** 15

for i in range(len_S):
    c[S[i]] -= 1
    temp = left_W + c['E']
    ans = min(ans,temp)

    if S[i] == 'W':
        left_W += 1

print(ans)

