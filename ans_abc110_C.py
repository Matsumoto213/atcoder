n = int(input())
lst = list(map(int, input().split()))
 
ans = 0
for a in lst:
    while a % 2 == 0:
        a //= 2
        ans += 1
print(ans)