# もっと計算量を少なくする
# リストの中で連続するK個のうち最も大きいKのリストを見つけるにはこれ以外の方法はないのか？
N,K = map(int, input().split())
p = list(map(int, input().split()))
su = -10 ** 9 + 7
idx = 0
for i in range(N - K + 1):
    temp = sum(p[i:i + K])
    if su < temp:
        idx = i
        su = temp

A = p[idx:idx + K]
tem = 0

for i in A:
    tem += (i + 1) / 2
print(tem) 
    