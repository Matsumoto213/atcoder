N = int(input())
S = [input() for _ in range(N)]
S = S[::-1]

for i in range(N):
    print(S[i])