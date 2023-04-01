N = int(input())
S = [input() for _ in range(N)]
C = {}
for i in range(N):
    if S[i] not in C:
        C[S[i]] = 1
    else:
        C[S[i]] += 1
C = dict(sorted(C.items()))
max_ = max(C.values())

for key,value in C.items():
    if value == max_:
        print(key)