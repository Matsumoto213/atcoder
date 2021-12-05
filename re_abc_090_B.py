A,B = map(int,input().split())
ans = 0

for i in range(A, B + 1):
    i = str(i)
    s = i[::-1]
    if i == s:
        ans += 1
print(ans)
    
    