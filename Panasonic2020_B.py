h, w = map(int, input().split())
if h == 1 or w == 1:
    ans = 1
elif (h * w) % 2 == 1:
    ans = h * w // 2 + 1
else:
    ans = h * w // 2
print(ans)
