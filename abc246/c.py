N,k,x = map(int, input().split())
A = list(map(int, input().split()))
# N個の商品
# A[i]が値段
# K枚のクーポン
# クーポンを使用するとa円のものがmax(0,a - kx)となる
# A.sort()
# 一回のループで残り枚数と全体を考えて、今使うべきかを判断する必要がある
for i in range(N):
    m = min(k, A[i] // x)
    A[i] -= x * m
    k -= m
A.sort(reverse = True)

for i in range(N):
    if 0 < k:
        A[i] = 0
        k -= 1
print(sum(A))
