# こういうループで見つけられない場合には共通点を見つける
# それができない場合には余りに目を向ける
N,K = map(int, input().split())
ans = N % K

a = abs(ans - K)
print(ans,a)
print(min(ans,a))
