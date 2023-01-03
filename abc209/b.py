N,X = map(int, input().split())
a = list(map(int, input().split()))
idx = 0
while True:
    if X <= 0 or len(a) <= idx:
        break

    if idx % 2 != 0:
        a[idx] -= 1
        X -= a[idx]
    else:
        X -= a[idx]
    idx += 1
    if X < 0:
        print('No')
        exit()
print('Yes')