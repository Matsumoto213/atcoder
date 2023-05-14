N = int(input())
S = input()

ans = -1
temp = 0
for i in range(N):
    if S[i] == 'o':
        temp += 1
    else:
        temp = 0
    if temp > ans:
        ans = temp

if 'o' in S and '-' in S:
    print(ans)
else:
    print(-1)