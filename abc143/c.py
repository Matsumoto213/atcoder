N = int(input())
S = input()
ans = []
temp = ''
for i in range(N):
    if S[i] != temp:
        ans.append(S[i])
    temp = S[i]
print(len(ans)) 