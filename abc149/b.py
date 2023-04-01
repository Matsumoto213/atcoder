a,b,k = map(int, input().split())
takahashi = max(0,a - min(a,k))

if takahashi > 0:
    aoki = b
else:
    aoki = max(0,b - (k - a))

print(takahashi, aoki)