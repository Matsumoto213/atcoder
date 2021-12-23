# 例外処理に苦戦している
N = int(input())
dis = [False] * N

for i in range(N):
    t,x,y = map(int,input().split())
    temp = x + y
    
    if temp <= t:
        # 偶数でかつtempが偶数の場合
        if t % 2 == 0 and temp % 2 == 0:
            dis[i] = True
        # 奇数でかつtempも奇数の場合
        elif t % 2 != 0 and temp % 2 != 0:
            dis[i] = True
        # 奇数でかつtempが偶数の場合
        elif t % 2 != 0 and temp % 2 == 0:
            pass
        # 偶数でかつtempが奇数の場合
        else:
            pass

ans = dis.count(True)
print("Yes" if ans == N else "No")