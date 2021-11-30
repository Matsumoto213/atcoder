H = int(input())

cnt = 1
ans = 0

while H > 0:
    ans += cnt
    H /= 2
    cnt *= 2
print(ans)