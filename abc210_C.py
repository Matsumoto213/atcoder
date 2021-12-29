# setにして崩すこともできない
# ソートして並び替えることもできない
# その中で計算量を少なくするにはどうすればいいのか？
# あまりいい問題ではない

N,K = map(int, input().split())
C = list(map(int, input().split()))
ans = -10 ** 9 + 7

for i in range(N):
    L = C[i:i + K]
    temp = len(set(L))
    ans = max(temp,ans)
print(ans)