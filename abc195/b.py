A, B, W = map(int, input().split())
W *= 1000

dp_min = [float('inf')] * (W + 1)
dp_min[0] = 0

for i in range(A, B+1):
    for j in range(W, i-1, -1):
        dp_min[j] = min(dp_min[j], dp_min[j-i]+1)

if dp_min[W] == float('inf'):
    print("UNSATISFIABLE")
else:
    print(dp_min[W])
