N = int(input())
S = [input() for _ in range(N)]
s = list(set(S))
dct = {}
for i in range(len(s)):
    dct[s[i]] = 0


for i in range(N):
    if dct[S[i]] == 0:
        print(S[i])
        dct[S[i]] += 1
    else:
        print(str(S[i])+ "(" + str(dct[S[i]]) + ")")
        dct[S[i]] += 1