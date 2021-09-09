n,s,d = map(int, input().split())
# nは高橋くんが使える呪文の数
# s秒以上かかる呪文や威力やd以下の呪文ではダメージを与えられない

ans = False
for i in range(n):
    x,y = map(int, input().split())
    if x < s and d < y:
        ans = True
        break

if ans == True:
    print("Yes")
else:
    print("No")
