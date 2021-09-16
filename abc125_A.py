a,b,t = map(int, input().split())
minute = a
count = t
ans = 0

while True:
    if a > t + 0.5:
        break
    a += minute
    ans += b
print(ans)