W,H,x,y = map(int, input().split())

ans = (H * W) / 2

if x * 2 == W and y * 2 == H:
    flag = 1
else:
    flag = 0

print(ans, flag)