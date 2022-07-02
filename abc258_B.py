N = int(input())

a = []

for i in range(N):
    A = list(map(int, input().split()))
    a.append(A)
ma = -10 ** 9
for i in range(N):
    for j in range(N):
        print(a[i][j])
        if a[i][j] > ma:
            ma = max(ma,int(a[i][j]))
            max_i = i
            max_j = j
print(max_i,max_j)
