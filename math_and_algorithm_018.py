N = int(input())
A = list(map(int, input().split()))
a,b,c,d = 0,0,0,0

for x in A:
    if x == 100:
        a += 1
    elif x == 200:
        b += 1
    elif x == 300:
        c += 1
    else:
        d += 1

ans = a * d + b * c

print(ans)
