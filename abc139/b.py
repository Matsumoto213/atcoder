a,b = map(int, input().split())
n = 0
ans = 0

if b == 1 or b == 0:
    print(ans)
    exit(0)

while True:
    if n >= b:
        break

    if ans != 0:
        n += a - 1
    else:
        n += a

    ans += 1

print(ans)