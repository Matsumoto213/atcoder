N = int(input())
S = list(input())
Q = int(input())
for _ in range(Q):
    t,a,b = map(int, input().split())

    if t == 1:
        temp = S[a - 1]
        S[a - 1] = S[b - 1]
        S[b - 1] = temp

    else:
        S = S[N:] + S[:N]
print(''.join(S))

        
