S = input()
T = input()
len_S = len(S)
len_T = len(T)
if len_S <= len_T:
    if T.startswith(S):
        print('Yes')
    else:
        print('No')
else:
    print('No')