N, A, B = map(int, input().split())
min_ = A * (N - 1) + B
max_ = B * (N - 1) + A
print(max(max_ - min_ + 1, 0))
    
