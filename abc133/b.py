N,d = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

def is_square_num(n):
    i2 = 0
    for i in range(0, n + 1):
        if i2 == n:
            return True
        if i2 > n:
            return False
        i2 += i * 2 + 1

ans = 0
for i in range(N - 1):
    for j in range(i + 1,N):
        x_dif = (X[i][0] - X[j][0]) ** 2
        y_dif = (X[i][1] - X[j][1]) ** 2
        temp = x_dif + y_dif
        if is_square_num(temp):
            ans += 1
print(ans)