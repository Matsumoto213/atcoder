N,Q = map(int, input().split())
A = list(map(int, input().split()))
K = [int(input()) for _ in range(Q)]
ma_ = max(K)
B = [0]
idx = 1
while True:
    if len(B) == ma_ + 1:
        break
    if idx not in A:
        B.append(idx)

    idx += 1
    
for i in K:
    print(B[i])