import heapq
N = int(input())
A = [int(input()) for _ in range(N)]

max_ = (heapq.nlargest(2,A))

for i in range(N):
    if A[i] == max_[0]:
        print(max_[1])
    else:
        print(max_[0])