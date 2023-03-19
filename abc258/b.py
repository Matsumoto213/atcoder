N = int(input())
A = [input() for _ in range(N)]

dx = [0,0,1,1,1,-1,-1,-1]
dy = [-1,1,1,0,-1,1,0,-1]
max_ = '0'

for i in range(N):
    for j in range(N):
        for d in range(8):
            # どの方向に進むかを決める
            height,width = dx[d],dy[d]
            temp = ""
            for l in range(N):
                x = (i + height * l) % N
                y = (j + width * l) % N
                temp += A[x][y]
            max_ = max(max_, temp)
print(max_)