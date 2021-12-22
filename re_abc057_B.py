N,M = map(int, input().split())
A = []
B = []
for _ in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

C = []
D = []
for _ in range(M):
    c,d = map(int, input().split())
    C.append(c)
    D.append(d)

P = []
for i in range(N):
    ans = 10 ** 9
    point = 0
    for j in range(M):
        dis = abs(A[i] - C[j]) + abs(B[i] - D[j])
        if dis < ans:
            point = j + 1
            ans = dis
    P.append(point)

for p in P:
    print(p)
    
                