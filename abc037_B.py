N,Q = map(int, input().split())
L = [0]* N

for i in range(Q):
    l,r,t = map(int, input().split())
    L[l - 1:r] = [t]* (r - l + 1)

for j in range(N):
    print(L[j])
 
    