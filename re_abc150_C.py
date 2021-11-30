import itertools

N = int(input())

P = list(map(int, input().split()))
Q = list(map(int, input().split()))
A = []

for i in range(1, N + 1):
    A.append(i)
    
per = itertools.permutations(A,N)

for idx,x in enumerate(per):
    idx += 1
    x = list(x)
    
    if x == P:
        P_id = idx
    
    if x == Q:
        Q_id = idx

print(abs(P_id - Q_id))