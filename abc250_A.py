h,w = map(int, input().split())
r,c = map(int, input().split())

ans = 0
for i in range(h):
    for j in range(w):
        temp = abs(i + 1 - r) + abs(j + 1 - c)
        if temp == 1:
           ans += 1
print(ans)