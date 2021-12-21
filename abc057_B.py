N,M = map(int, input().split())

A = []
B = []
C = []
D = []
for _ in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

for i in range(M):
    c,d = map(int, input().split())
    C.append(c)
    D.append(D)

for i in range(N):
    ans = 10 ** 8
    for j in range(N):
        i_manha = abs(A[i] - C[j] + B[i] - D[j])
        if ans > i_manha:
            ans = i_manha
            idx = j + 1
    print(idx)
         
        
    