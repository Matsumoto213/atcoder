a,b,c,d,e,f,x = map(int, input().split())

taka = 0
rest = 0
while True:
    if taka + rest >= x:
        break
    taka += min(a,x - taka - rest)
    rest += c

ao = 0
r = 0
while True:
    if ao + r >= x:
        break
    ao += min(d,x - ao - r)
    r += f

if taka * b > ao * e:
    print('Takahashi')
elif taka * b < ao * e:
    print('Aoki')
else:
    print('Draw')