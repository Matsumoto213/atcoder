N = int(input())
S = list(input())
S.insert(0, 0)
for i in range(1,N):
    temp = N - i
    ans = 0
    for j in range(1, temp + 1):
        if S[j] != S[j + i]:
            ans += 1
        else:
            break
    print(ans)