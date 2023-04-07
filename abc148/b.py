N = int(input())
S,T = input().split()

ans = ''

for i in range(N):
    ans = ans + S[i]
    ans = ans + T[i]
print(ans)