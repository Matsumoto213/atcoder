N,K,Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]
S = [K - Q] * N

for i in A:
    S[i - 1] += 1

for j in S:
    if j > 0:
        print("Yes")
    else:
        print("No")
        