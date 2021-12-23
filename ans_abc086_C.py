# この問題で詰まった点
# 最後の一文が解けなかったのだが、地点は必ずしも0から始まるわけでは無いため
# 地点をそれぞれ更新していく必要がある
N = int(input())
t0, x0, y0 = 0,0,0

for i in range(N):
    t, x, y = map(int,input().split())
    
    dis = abs(x - x0) + abs(y - y0)
    time = t - t0
    
    if time - dis < 0 or (time - dis) % 2 == 1:
        print("No")
        break
    t0, x0, y0 = t, x, y
else:
    print("Yes")