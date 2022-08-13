N,W = map(int, input().split())
A = [0,0,0] + list(map(int, input().split()))

N += 3
ans = set()

for i in range(N):
    for j in range(i + 1, N):
        for l in range(j + 1, N):
            temp = A[i] + A[j] + A[l]
            if temp <= W:
                ans.add(temp)
print(len(ans) - 1)