def count_subsets(N, M, S, C):
    ans = 0
    for i in range(2 ** M):
        L = set()
        for j in range(M):
            if ((i >> j) & 1):
                for k in range(len(S[j])):
                    L.add(S[j][k])
        if C == L:
            ans += 1
    return ans

N,M = map(int, input().split())
S = []
compare = set([i + 1 for i in range(N)])
for i in range(M):
    c = int(input())
    C = list(map(int, input().split()))
    S.append(C)
print(count_subsets(N, M, S, compare))