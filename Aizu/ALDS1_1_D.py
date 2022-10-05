N = int(input())
R = [int(input()) for _ in range(N)]

max_ = -10 ** 16 + 8
min_ = R[0]
for i in range(1,N):
    max_ = max(max_, R[i] - min_)
    min_ = min(min_,R[i])
    print(min_,max_)
