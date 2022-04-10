S = input()
N = len(S)
L = ['x']
ans = 0
i = 0

while True:
    if i >= N:
        break
    if S[i] != L[ans]:
        L.append(S[i])
        i += 1
    else:
        L.append(S[i: i + 2])
        i += 2
    ans += 1

if L[-2] == L[-1]:
    print(len(L) - 2)
else:
    print(len(L) - 1)