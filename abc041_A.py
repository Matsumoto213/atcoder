n,a,b = map(int, input().split())



if a % 2 == b % 2:
    ans = (b - a) // 2
else:
    pa = (a - 1 + 1) + (b - a) // 2
    pb = (n - b + a) + (b - a) // 2
    print(pa,pb)
    ans = min(pa,pb)