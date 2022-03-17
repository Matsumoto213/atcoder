N = int(input())
S = input()
mod = 10 ** 9 + 7
from collections import defaultdict
dic=defaultdict(int)

for i in range(N):
    dic[S[i]] += 1

ans = 1
for y in dic.keys():
    temp = dic[y] + 1
    print(temp)
    ans *= temp
    ans %= mod


print((ans + mod - 1) % mod)
