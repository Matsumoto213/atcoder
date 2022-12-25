S = input()
s = ''

for i in range(len(S)):
    if S[i] == '(':
        pass
    elif S[i] == ')':
        s = ''
    else:
        if S[i] in s:
            print('No')
            exit()
        else:
            s += S[i]
print('Yes')