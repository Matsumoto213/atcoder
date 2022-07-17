n,x,y = map(int, input().split())

if n <= 1:
    print(0)
else:
    print((x * y) ** (n - 1) + x * y ** (n - 1))