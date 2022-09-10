def judgeSplit(colums):
    for i in range(7):
        for j in range(i):
            if colums[i] and colums[j]:
                for k in range(j + 1,i):
                    if not column[k]:
                        return 'Yes'
    return 'No'

S = input()
S = '$' + S
if S[1] == '1':
    print('No')
    exit()
else:
    column = [False] * 7
    column[0] = (S[7] == '1')
    column[1] = (S[4] == '1')
    column[2] = (S[2] == '1') or (S[8] == '1')
    column[3] = (S[1] == '1') or (S[5] == '1')
    column[4] = (S[3] == '1') or (S[9] == '1')
    column[5] = (S[6] == '1')
    column[6] = (S[10] == '1')
    print(judgeSplit(column))
