w,a,b = map(int, input().split())
a_w = a + w
b_w = b + w

ans = 0
if a < b:
    ans =b - a_w
elif a > b:
    ans = a - b_w

if ans > 0:
    print(ans)
else:
    print(0)