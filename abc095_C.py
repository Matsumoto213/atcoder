a,b,ab,x,y = map(int, input().split())

ans = 0
bigger = max(x,y)
small = min(x,y)
if a + b > ab * 2:
    ans1 = ab * (bigger * 2)
    ans2 = ab * abs(small * 2)
    x -= small
    y -= small
    if x > 0:
        ans2 += x * int(a)
    elif y > 0:
        ans2 += y * b
    ans = min(ans1,ans2)
else:
    ans1 = a * x
    ans2 = b * y
    ans = ans1 + ans2
print(ans)