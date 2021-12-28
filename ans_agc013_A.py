n = int(input())
an = list(map(int, input()).split())
p = a[0]

res = 1
pinc = 0
inc = 0

for i in a[1::]:
    if p < i:
        inc = 1
    elif p > i:
        inc = -1
    
    if pinc * inc == -1:
        res += 1
        inc = 0
    pinc = inc
    p = i
print(res)