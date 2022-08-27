x,y,n = map(int, input().split())
ans = 0
cnt = 0

if n < 3:
    print(x * n)
    exit()

while n:
    temp = min(n,3)
    if temp == 3:
        tem = min(x * temp,y)
    else:
        tem = min(x * temp, y / temp)
    n -= temp
    ans += tem
print(ans)