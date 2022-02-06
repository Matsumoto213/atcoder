import itertools
N = int(input())
A = list(map(int, input().split()))
ans = 0

# 5枚選ぶ場合など枚数を指定されている場合はcombinationを選んだ方がいい
for l in itertools.combinations(list(range(N)), 5):
    s = 0
    for i in l:
        s += A[i]
    if s == 1000 : ans += 1
print(ans)