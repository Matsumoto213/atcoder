N = int(input())
a = list(map(int, input().split()))
L = []
ans = 0

for i in range(N):
    if i in L:
        continue
    temp = a[i]
    if a[temp - 1] == i + 1:
        ans += 1
        L.append(temp - 1)
    
print(ans)