N = int(input())
A = []
B = []

for i in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

min_A = A.index(min(A))
min_B = B.index(min(B))

A.sort()
B.sort()

if min_A == min_B:
    print(min(A[0] + B[0], max(A[0], B[1])))
else:
    print(min(A[0],B[0]))
