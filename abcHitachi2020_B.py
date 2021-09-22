A,B,M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_a = min(a)
min_b = min(b)

cheap = min_a + min_b

for i in range(M):
    x,y,c =  map(int, input().split())
    ans = a[x - 1] + b[y - 1] - c

    cheap = min(cheap,ans)
print(cheap)


