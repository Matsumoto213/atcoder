N = int(input())
S = [int(input()) for _ in range(N)]
S.sort()
sum_s = sum(S)

if sum_s % 10 != 0:
    print(sum_s)
    exit(0)

for i in range(N):
    sum_s -= S[i]
    if sum_s % 10 != 0:
        print(sum_s)
        exit(0)
    else:
        sum_s += S[i]
print(0)


