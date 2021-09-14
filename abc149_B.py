a,b,k = map(int, input().split())


if a <= k:
    if b - (k - a) >= 0:
        print(0,b - (k - a))
    else:
        print(0,0)
else:
    print(a - k, b)