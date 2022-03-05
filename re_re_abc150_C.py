import itertools

N = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

L = [i for i in range(1, N + 1)]

for idx,v in enumerate(itertools.permutations(L,N)):
    v = list(v)
    if v == p:
        a = idx
    
    if v == q:
        b = idx

print(abs(a - b))
