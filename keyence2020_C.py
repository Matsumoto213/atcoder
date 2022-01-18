N,K,S = map(int, input().split())

A = []
for i in range(K):
    A.append(S)

temp = S + 1
if temp > 10 ** 9:
    temp = 1

for i in range(K,N):
    A.append(temp)

print(*A)
    