S = input()
all_pine_collapse_flg = [False] * 7

all_pine_collapse_flg[0] = S[6] == '0'
all_pine_collapse_flg[1] = S[3] == '0'
all_pine_collapse_flg[2] = (S[1] == '0') and (S[7] == '0')
all_pine_collapse_flg[3] = (S[0] == '0') and (S[4] == '0')
all_pine_collapse_flg[4] = (S[2] == '0') and (S[8] == '0')
all_pine_collapse_flg[5] = S[5] == '0'
all_pine_collapse_flg[6] = S[9] == '0'
if S[0] == '0':
    for i in range(6):
        if all_pine_collapse_flg[i] != True:
            for j in range(i + 1, 7):
                if all_pine_collapse_flg[j] != True:
                    for k in range(i + 1,j):
                        if all_pine_collapse_flg[k] == True:
                            print('Yes')
                            exit()

print('No')