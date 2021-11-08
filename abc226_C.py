N = int(input())

T = []
K = []
A = []

for i in range(N):
    t,k,*a = map(int, input().split())
    T.append(t)
    K.append(k)
    A.append(a)

ans = T[N - 1]
idx = K[N - 1]
result = A[N - 1]

for i in result:
    i = i - 1
    ans += T[i]
print(ans)