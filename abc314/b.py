N = int(input())

from collections import defaultdict
ab = defaultdict(list)

betNum = []
for i in range(N):
    C = int(input())
    A = list(map(int, input().split()))

    for j in A:
        ab[j].append(i + 1)
    betNum.append(C)
X = int(input())

bet = ab[X]
min_ = 10 ** 8 + 7

for i in bet:
    min_ = min(min_,betNum[i - 1])

ans = 0
ansL = []
for i in bet:
    if betNum[i - 1] == min_:
        ans += 1
        ansL.append(i)

print(ans)
print(*ansL)