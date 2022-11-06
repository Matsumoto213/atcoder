N = int(input())
P = list(map(int,input().split()))

l = []

for i in range(1,N + 1):
    l.append(i)

def next_permutation(mi):
    if len(mi) <= 1:
        return False
    first_idx = 0
    last_idx = len(mi)
    i = last_idx - 1
    while True:
        ii = i
        i -= 1
        if mi[i] < mi[ii]:
            j = last_idx - 1
            while not mi[i] < mi[j]:
                j -= 1
            mi[i], mi[j] = mi[j], mi[i]
            mi[ii:last_idx] = mi[ii:last_idx][::-1]
            return True
        if i == first_idx:
            mi[first_idx:last_idx] = mi[first_idx:last_idx][::-1]
            return False
    return False

print(next_permutation(l))