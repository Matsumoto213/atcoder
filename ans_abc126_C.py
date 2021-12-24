# シンプルで素晴らしいコード
# whileで回数を自動的に数える
# 何回見ても素晴らしいコード
n,k =list(map(int, input().split()))
ans = 0
 
for i in range(n):
    z = i + 1
    tmp = 1 / n
    while z < k:
        z*=2
        tmp*=(1/2)
    ans+=tmp
print(ans)