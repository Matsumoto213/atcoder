N = int(input())
S = [int(input()) for i in range(N)]
s = sum(S)
S.sort()

if s % 10 != 0:
    print(s)
    exit()
else:
    for i in range(N):
        s -= S[i]
        if s % 10 != 0:
            print(s)
            exit()
        else:
            s += S[i]

print(0)
