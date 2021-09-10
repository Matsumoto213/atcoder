n,m,x =map(int, input().split())

a = list(map(int, input().split()))

ans = []
count = 0

for i in range(n + 1):
    if i in a:
        count += 1

    if i == x:
        ans.append(count)
        count = 0
    elif i == n:
        ans.append(count)
print(min(ans))