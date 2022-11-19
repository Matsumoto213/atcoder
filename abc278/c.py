H,M = input().split()

if len(H) == 1:
    H = '0' + H

if len(M) == 1:
    M = '0' + M

H = [int(H[i]) for i in range(2)]
M = [int(M[i]) for i in range(2)]
a,b,c,d = H[0],H[1],M[0],M[1]
while True:
    if (b < 6 and (a == 1 or a == 0)) or (b < 6 and c < 4 and a == 2):
        break
    d += 1

    if d == 10:
        c += 1
        d = 0
        
    if c == 6:
        c = 0
        b += 1
        
    if b == 10:
        b = 0
        a += 1

if c == d == 0:
    print(str(a)+str(b), str(c))
elif a == 0:
    print(str(b), str(c)+str(d))
else:
    print(str(a)+str(b), str(c)+str(d))