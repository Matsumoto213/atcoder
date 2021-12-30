from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
half = len(A) // 2
max_left = max(A[:half])
max_right = max(A[half:])

min_ = min(max_left,max_right)
print(A.index(min_) + 1)