N = int(input())
ans = 0

for i in range(1,N + 1):
    i = str(i)
    
    if len(i) % 2 != 0:
        ans += 1
print(ans)