x,y = map(int, input().split())
ans = 0
now = x

while now <= y:
    ans += 1
    now += now

print(ans)

