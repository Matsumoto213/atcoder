N,K = map(int, input().split())
S = input()
T = ''
ans = 0

for i in range(N):
    if S[i] == 'o' and ans < K:
        T = T + 'o'
        ans += 1
    else:
        T = T + 'x'
print(T)