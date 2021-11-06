from collections import Counter
N,K = map(int, input().split())
A = list(map(int, input().split()))

a = Counter(A)

# 何回出たかを大きい順に並び替える
x = sorted(a.values(),reverse = True)
ans = 0

for i in range(len(x)):
    if i >= K:
        ans += x[i]
print(ans)