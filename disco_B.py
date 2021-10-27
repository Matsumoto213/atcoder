N = int(input())
A = list(map(int, input().split()))


x = 0
y = sum(A)

m = y

for i in range(N):
    x += A[i]
    y -= A[i]
    m = min(m,abs(x - y))
print(m)
