n,x = map(int, input().split())
L = list(map(int, input().split()))
position = 0
ans = 1
for i in range(n):
    position += L[i]
    if position <= x:
        ans += 1
    else:
        print(ans)
        exit()
print(ans)