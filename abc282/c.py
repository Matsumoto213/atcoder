N = int(input())
S = input()
ans = 0
for i in range(N):
    if S[i] == '"':
        ans += 1

    if S[i] == ',' and ans % 2 == 0:
        print('.',end = "")
    else:
        print(S[i],end = "")