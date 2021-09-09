n = int(input())
A = []
B = []

for i in range(n):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)


ans = 10 ** 8

for i in range(n):
    for j in range(n):
        if i == j:
            ans1 = A[i] + B[j]
        else:
            ans1 = max(A[i],B[j])
        ans = min(ans,ans1)
print(ans)



