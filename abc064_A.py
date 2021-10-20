a,b,c = map(str, input().split())
ans = int(a + b + c)

if ans % 4 == 0:
    print("YES")
else:
    print("NO")