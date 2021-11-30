A,B,M = map(int, input().split())

a = list(map(int,input().split()))
b = list(map(int, input().split()))

min_a = min(a)
min_b = min(b)

ans = min_a + min_b

for _ in range(M):
    x,y,c = map(int, input().split())
    result = a[x - 1] + b[y - 1] - c
    ans = min(result, ans)
print(ans)
    
    