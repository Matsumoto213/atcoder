import itertools
N = int(input())
L = list(map(int, input().split()))
L.sort(reverse = True)
L = L[:3]
per = list(itertools.permutations(L,3))
ans = -10 ** 15 + 8
for v in per:
    temp = int("".join(map(str, v)))
    ans = max(temp,ans)
print(ans)