N = int(input())
P = list(map(int, input().split()))
max_ = 0
for i in range(1, N):
    max_ = max(P[i], max_)
print(max(0, max_ - P[0] + 1))
