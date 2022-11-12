N = int(input())
S = [input() for _ in range(N)]
ans = set(S)
for i in range(N):
    # print(S[i],S[i][0],S[i][1])
    if (S[i][0] != 'H') and (S[i][0] != 'D') and (S[i][0] != 'C') and (S[i][0] != 'S'):
        print('No')
        exit()

    if  S[i][1] != 'A' and S[i][1] != '2' and  S[i][1] != '3' and S[i][1] != '4' and  S[i][1] != '5' and  S[i][1] != '6' and S[i][1] != '7' and S[i][1] != '8' and  S[i][1] != '9' and S[i][1] != 'T' and S[i][1] != 'J' and  S[i][1] != 'Q' and S[i][1] != 'K':
        print('No')
        exit()

if len(ans) != len(S):
    print('No')
else:
    print('Yes')