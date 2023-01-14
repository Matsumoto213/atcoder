N = int(input())
P = list(map(int, input().split()))
def prev_permutation(N,P):
    i = N - 2
    while i >= 0 and P[i] <= P[i + 1]:
        i -= 1
    if i == -1:
        return None
    j = N - 1
    while P[j] >= P[i]:
        j -= 1
    P[i], P[j] = P[j], P[i]
    P[i + 1:] = reversed(P[i + 1:])
    return P

print(prev_permutation(N,P))