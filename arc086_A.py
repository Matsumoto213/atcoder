from collections import Counter
N,K= map(int, input().split())
L = list(map(int, input().split()))

C = Counter(L)
lenC = len(C)

# これで逆順にする
mc = C.most_common()[::-1]
ans = 0

for i in range(lenC - K):
    ans += mc[i][1]
print(ans)