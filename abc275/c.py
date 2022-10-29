import numpy as np
import math
S = [input() for _ in range(9)]
L = []

def IsOrthogonal(a,b):
    return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])

def IsRectangle(a,b,c,d):
    dist12 =  IsOrthogonal(a,b) 
    dist13 = IsOrthogonal(a,c)
    dist14 = IsOrthogonal(a,d)

    if(dist12 == dist13 and 2 * dist12 == dist14):
        dist = IsOrthogonal(b,d)
        return (dist == IsOrthogonal(c, d) and dist == dist12)
    
    if(dist13 == dist14 and 2 * dist13 == dist12):
        dist = IsOrthogonal(b,c)
        return (dist == IsOrthogonal(b, d) and dist == dist13)

    if(dist12 == dist14 and 2 * dist12 == dist13):
        dist = IsOrthogonal(b,c)
        return (dist == IsOrthogonal(c, d) and dist == dist12)

    return False

for i in range(9):
    for j in range(9):
        if S[i][j] == '#':
            L.append([i,j])
ans = 0
if len(L) >= 4:
    for i in range(len(L) - 3):
        for j in range(i + 1,len(L) - 2):
            for k in range(j + 1, len(L) - 1):
                for l in range(k + 1,len(L)):
                    if IsRectangle(L[i],L[k],L[j],L[l]):
                        ans += 1
else:
    print(0)
    exit()

print(ans)