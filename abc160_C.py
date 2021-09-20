k,n = map(int, input().split())
lst = list(map(int, input().split()))

ans = (k - a[-1]) + a[0]

for i in reversed(range(1, n)):
    x = a[i] - a[i - 1]

    if x > ans:
        ans = x
        
print(k - ans)
