N = int(input())
A = [input() for _ in range(N)]

ans = "0"

dx = [0,0,1,1,1,-1,-1,-1]
dy = [-1,1,1,0,-1,1,0,-1]

for i in range(N):
    for j in range(N):
        # それぞれのマスに対して8方向進む
        for d in range(8):
            num = ""
            for k in range(N):
                print(i,j,dx[d],dy[d],k)
                x = (i + dx[d] * k) % N
                y = (j + dy[d] * k) % N
                num += A[x][y]
                print(num)
            ans = max(ans, num)
print(ans)
